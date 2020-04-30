from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TicketTimesheet(models.Model):
    _inherit = 'helpdesk.ticket'

    project = fields.Many2one(
        comodel_name = 'project.project',
        string = 'project_id',
    )
    
    task = fields.Many2one(
        comodel_name = 'project.task',
        string = 'task',
    )

    timesheet_ids = fields.One2many(
        comodel_name='account.analytic.line',
        inverse_name='ticket_id',
        string='Timesheet',
    )

    ##### REVISAR NO FUNCIONA #####
    #total_computed_hours_ticket = fields.Float(computed='compute_hours')
#
    #@api.depends('computed_hours')
    #def compute_hours(self):
    #    for task in self:
    #        task.total_computed_hours_ticket = sum(task.sudo().mapped('computed_hours'))

    total_hours_ticket = fields.Float(compute='impute_hours')

    @api.depends('timesheet_ids.unit_amount')
    def impute_hours(self):
        for task in self:
            task.total_hours_ticket = sum(task.sudo().timesheet_ids.mapped('unit_amount'))

    # Si cambia el Proyecto resetea la Tarea
    @api.onchange('project')
    def _onchange_project(self):
        self.task = False