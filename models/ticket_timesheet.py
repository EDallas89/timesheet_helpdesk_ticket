from odoo import models, fields, api
from datetime import datetime

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'


    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )

    #@api.onchange('partner_id')
    #def _onchange_partner_id(self):
    #    partner_id = self.env.partner_id
    ############################# REVISAR ##############################
    #total_hours_ticket = fields.Float(string='Total Hours')
