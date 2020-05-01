from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project',
    )
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task',
    )
    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )
    total_computed_hours_ticket = fields.Float(
        compute='compute_hours',
        string='Computed Hours'
    )
    partner_phone = fields.Char(
        string='Contact Phone',
        related='partner_id.mobile',
        store=True,
        readonly=False,
    )

    def compute_hours(self):
        for record in self:
            record.total_computed_hours_ticket = \
                sum(record.mapped('timesheet_ids.computed_hours'))

    total_hours_ticket = fields.Float(compute='impute_hours')

    @api.depends('timesheet_ids.unit_amount')
    def impute_hours(self):
        for record in self:
            record.total_hours_ticket = sum(record.timesheet_ids.mapped('unit_amount'))

    @api.onchange('project')
    def _onchange_project(self):
        self.task = False
