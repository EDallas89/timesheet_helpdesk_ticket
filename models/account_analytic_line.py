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
    start_stop = fields.Boolean(
        string='Start Stop'
    )
    date_start = fields.Datetime(
        string='Start Time'
    )
    date_stop = fields.Datetime(
        string='End Time'
    )
    date_reboot = fields.Datetime(
        string='Reboot Time'
    )
    computed_hours = fields.Float(
        string='Computed Hours'
    )

    @api.multi
    def action_start(self):
        date_start = self.date_start
        if date_start == False:
            return self.write({'date_start': datetime.now(), 'start_stop': True})
        else:
            return self.write({'date_pause': datetime.now(), 'start_stop': True})

    @api.multi
    def count_time(self):
        date_reboot = self.date_reboot
        if date_reboot:
            datetime_diff = datetime.now() - date_reboot
            self.date_reboot = False
        else:
            datetime_diff = datetime.now() - self.date_start
        minutes, seconds = divmod(datetime_diff.total_seconds(), 60)

        # Convertimos los minutos en horas
        hours, minutes = divmod(minutes, 60)
        # Damos formato a la hora
        dur_hours = (('%0*d') % (2, hours))
        dur_minutes = (('%0*d') % (2, minutes * 1.677966102))
        duration = dur_hours + '.' + dur_minutes

        return duration

    @api.multi
    def action_pause(self):
        duration = self.count_time()

        if self.unit_amount == self.computed_hours:
            return self.write({
                'start_stop': False,
                'computed_hours': duration,
                'unit_amount': duration,
            })

        return self.write({
            'start_stop': False,
            'computed_hours': duration,
        })

    @api.multi
    def action_stop(self):
        duration = self.count_time()
        if self.unit_amount == self.computed_hours:
            return self.write({
                'start_stop': False,
                'date_stop': datetime.now(),
                'computed_hours': duration,
                'unit_amount': duration,
            })

        return self.write({
            'start_stop': False,
            'date_stop': datetime.now(),
            'computed_hours': duration,
        })
