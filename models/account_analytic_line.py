from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime, timedelta, date

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    ticket_id = fields.Many2one(
        comodel_name='helpdesk.ticket',
        string='ticket_id',
    )
    date_start = fields.Datetime('Start Time')
    start_stop = fields.Boolean(string='Start Stop', default=False)
    #date_stop = fields.Datetime('End Time')

    # Definimos la funcionalidad del botón Start
    @api.multi
    def action_start(self):
        # Comprobamos si el valor de start_stop es true y si el usuario es el usuario actual
        # search_count devuelve un entero con el número de condiciones ciertas
        action_click = self.search_count([('start_stop', '=', True), ('user_id', '=', self.env.user.id)])
        # Si alguna de las condiciones es cierta devuelve un mensaje de error
        if action_click <= 0:
            # Imprime un mensaje en el chatter
            #message = _("Started by %s.") % (self.env.user.name)
            #self.message_post(body=message)
            # Devuelve la fecha actual
            return self.write({'date_start':fields.datetime.now(), 'start_stop':True})

        else: 
            raise exceptions.UserError('You cannot start multiple Ticket. Another Ticket is already in progress.')