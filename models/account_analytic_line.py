from odoo import models, fields, api
from datetime import datetime
import math

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _order = 'date_start asc'

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket_id',
    )
    # Campos para la Vista Tree
    start_stop = fields.Boolean(string='Start Stop', default=False)
    date_start = fields.Datetime('Start Time')
    date_stop = fields.Datetime('End Time')
    date_reboot = fields.Datetime('Reboot Time')
    computed_hours = fields.Float('Computed Hours')

    # Cambia el valor de start_stop a True y escribe la fecha y hora actual en el campo date_start. Si el campo date_start ya tiene valor no lo modifica.
    @api.multi
    def action_start(self):
        date_start = self.date_start
        if (date_start==False):
            return self.write({'date_start':datetime.now(), 'start_stop':True})
        else:
            return self.write({'date_pause': datetime.now(), 'start_stop':True})
                
    # Cuenta las horas y minutos entre dos fechas. Si hay una fecha de reinicio tomará esta, sino utilizará la fecha de inicio
    @api.multi
    def count_time(self):
        date_reboot = self.date_reboot
        # Si hay fecha de reinicio calcula de diferencia entre ella y la fecha actual y resetea la fecha de reinicio
        if (date_reboot!=False):
            datetime_diff = datetime.now() - self.date_reboot
            self.date_reboot=False
        # Si no hay fecha de reinicio calcula la diferencia entre la fecha de incio y la fecha actual
        else:
        # Comparamos la fecha actual con la fecha de Start, convirtiendola en String
            datetime_diff = datetime.now() - self.date_start

        # Convertimos los segundos totales entre Start y Stop en minutos
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60)
                               
        # Convertimos los minutos en horas
        hours, minutes = divmod(minutes, 60)
        # Damos formato a la hora
        dur_hours = (('%0*d')%(2,hours))
        dur_minutes = (('%0*d')%(2,minutes*1.677966102))
        duration = dur_hours+'.'+dur_minutes

        return duration

    # Llama a la funbción count_time. El resultado lo graba en el campo unit_amount.
    # Pone el campo start_stop en False.
    @api.multi
    def action_pause(self):
        duration = self.count_time()
        # Comprueba si el valor de unit_amount es igual a computed_hours, si no es igual (porque ha sido modificado a mano) no modifica el campo.
        if (self.unit_amount == self.computed_hours):
            values = self.write({
            'start_stop':False, 
            'computed_hours':duration,
            'unit_amount':duration,
            })
        else:
             values = self.write({
            'start_stop':False, 
            'computed_hours':duration,
            })

    # Llama a la función count_time. El resultado lo graba en el campo unit_amount.
    # Pone el campo start_stop en False y graba date_stop.
    @api.multi
    def action_stop(self):
        duration = self.count_time()
        # Comprueba si el valor de unit_amount es igual a computed_hours, si no es igual (porque ha sido modificado a mano) no modifica el campo.
        if (self.unit_amount == self.computed_hours):
            values = self.write({
            'start_stop':False, 
            'date_stop':datetime.now(), 
            'computed_hours':duration,
            'unit_amount':duration,
            })
        else:
             values = self.write({
            'start_stop':False, 
            'date_stop':datetime.now(), 
            'computed_hours':duration,
            })

        return values

    