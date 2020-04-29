from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    project = fields.Many2one(
        comodel_name = 'project.project',
        string = 'Project',
    )
    task = fields.Many2one(
        comodel_name = 'project.task',
        string = 'Task',
    )

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )

    total_hours_ticket = fields.Float(compute='compute_hours', string='Total Hours')

    @api.depends('timesheet_ids.unit_amount')
    def compute_hours(self):
        for task in self:
            task.total_hours_ticket = sum(task.sudo().timesheet_ids.mapped('unit_amount'))