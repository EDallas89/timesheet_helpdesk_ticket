from odoo import models, fields, api
from datetime import datetime

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='timesheet_ids',
    )
    
    ############################ REVISAR ##############################
    total_hours_ticket = fields.Datetime(compute='total_hours', store=True, string='Total Hours')

    @api.onchange('unit_amount')
    def _onchange_unit_amount(self):
        return 5
    