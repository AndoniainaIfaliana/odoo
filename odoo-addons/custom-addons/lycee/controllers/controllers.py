# -*- coding: utf-8 -*-
# from odoo import http


# class Lycee(http.Controller):
#     @http.route('/lycee/lycee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lycee/lycee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lycee.listing', {
#             'root': '/lycee/lycee',
#             'objects': http.request.env['lycee.lycee'].search([]),
#         })

#     @http.route('/lycee/lycee/objects/<model("lycee.lycee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lycee.object', {
#             'object': obj
#         })
