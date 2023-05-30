# -*- coding: utf-8 -*-
# from odoo import http


# class Esearch(http.Controller):
#     @http.route('/esearch/esearch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/esearch/esearch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('esearch.listing', {
#             'root': '/esearch/esearch',
#             'objects': http.request.env['esearch.esearch'].search([]),
#         })

#     @http.route('/esearch/esearch/objects/<model("esearch.esearch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('esearch.object', {
#             'object': obj
#         })
