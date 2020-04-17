from odoo import models, fields, api
from datetime import datetime, timedelta, date
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


class AccountAnalyticLine(models.Model):
    _inherit = ['account.analytic.line']

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket_id',
    )

    start_stop = fields.Boolean(string='Start Stop', default=False)
    date_start = fields.Datetime('Start Time')
    date_stop = fields.Datetime('End Time')

    # Escribe la fecha y hora actual en el campo date_start
    @api.multi
    def action_start(self):
        return self.write({'date_start':datetime.now(), 'start_stop':True})
    

    # Escribe la fecha y hora actual en el campo date_stop. 
    # Calcula la diferencia entre date_start y date_stop y la escribe en el campo   unit_amount.
    # Recalcula las horas totales del ticket sumando los unit_amount
    @api.multi
    def action_stop(self):
        # Comparamos la fecha actual con la fecha de Start, convirtiendola en String
        datetime_diff = datetime.now() - self.date_start
        # Convertimos los segundos totales entre Start y Stop en minutos
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60)
        # Convertimos los minutos en horas
        hours, minutes = divmod(minutes, 60)
        dur_hours = (('%0*d')%(2,hours))
        dur_minutes = (('%0*d')%(2,minutes*1.677966102))
        duration = dur_hours+'.'+dur_minutes

        ######################### REVISAR #############################
        for unit_amount in self:
            total_hours = total_hours + unit_amount

        return self.write({
            'start_stop':False, 
            'date_stop':datetime.now(), 
            'unit_amount':duration,
            'total_hours_ticket':total_hours})
