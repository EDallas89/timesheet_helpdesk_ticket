from odoo import models, fields, api
from datetime import datetime


class AccountAnalyticLine(models.Model):
    _inherit = ['account.analytic.line']

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket_id',
    )

    start_stop = fields.Boolean(string='Start Stop', default=False)
    # 0 - Sin Iniciar - Muestra Play
    # 1 - Iniciado - Muestra Pause y Stop
    # 2 - Pausado - Muestra Play y Stop
    # 3 - Finalizado - No muestra botones
    date_start = fields.Datetime('Start Time')
    date_stop = fields.Datetime('End Time')

    # Cambia el valor de start_stop a True y escribe la fecha y hora actual en el campo date_start. Si el campo date_start ya tiene valor no lo modifica.
    @api.multi
    def action_start(self):
        date_start = self.date_start
        if (date_start==False):
            return self.write({'date_start':datetime.now(), 'start_stop':True})
        else:
            return self.write({'start_stop':True})
        
    
    # Escribe la fecha y hora actual en el campo date_stop. 
    # Calcula la diferencia entre date_start y date_stop y la escribe en el campo   unit_amount.
    # Recalcula las horas totales del ticket sumando los unit_amount
    @api.multi
    def action_stop(self):
        # Comparamos la fecha actual con la fecha de Start, convirtiendola en String
        datetime_diff = datetime.now() - self.date_start
        # Convertimos los segundos totales entre Start y Stop en minutos
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60)
        hours, minutes = divmod(minutes, 60)
        # Convertimos los minutos en horas
        dur_hours = (('%0*d')%(2,hours))
        dur_minutes = (('%0*d')%(2,minutes*1.677966102))
        duration = dur_hours+'.'+dur_minutes

        return self.write({
            'start_stop':False, 
            'date_stop':datetime.now(), 
            'unit_amount':duration
            })