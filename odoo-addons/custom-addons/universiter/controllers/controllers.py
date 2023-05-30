# -*- coding: utf-8 -*-
# from odoo import http


# class Universiter(http.Controller):
#     @http.route('/universiter/universiter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/universiter/universiter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('universiter.listing', {
#             'root': '/universiter/universiter',
#             'objects': http.request.env['universiter.universiter'].search([]),
#         })

#     @http.route('/universiter/universiter/objects/<model("universiter.universiter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('universiter.object', {
#             'object': obj
#         })
