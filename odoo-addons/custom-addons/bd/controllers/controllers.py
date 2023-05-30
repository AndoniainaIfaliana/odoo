# -*- coding: utf-8 -*-
# from odoo import http


# class Bd(http.Controller):
#     @http.route('/bd/bd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bd/bd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bd.listing', {
#             'root': '/bd/bd',
#             'objects': http.request.env['bd.bd'].search([]),
#         })

#     @http.route('/bd/bd/objects/<model("bd.bd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bd.object', {
#             'object': obj
#         })
