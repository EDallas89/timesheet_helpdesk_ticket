# -*- coding: utf-8 -*-
from odoo import http

# class ModHelpdesk(http.Controller):
#     @http.route('/mod_helpdesk/mod_helpdesk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mod_helpdesk/mod_helpdesk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mod_helpdesk.listing', {
#             'root': '/mod_helpdesk/mod_helpdesk',
#             'objects': http.request.env['mod_helpdesk.mod_helpdesk'].search([]),
#         })

#     @http.route('/mod_helpdesk/mod_helpdesk/objects/<model("mod_helpdesk.mod_helpdesk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mod_helpdesk.object', {
#             'object': obj
#         })