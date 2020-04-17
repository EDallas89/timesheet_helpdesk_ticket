from odoo import models, fields, api

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='timesheet_ids',
    )
    
    ############################ REVISAR ##############################
    total_hours_ticket = fields.Float(string='Total Hours')