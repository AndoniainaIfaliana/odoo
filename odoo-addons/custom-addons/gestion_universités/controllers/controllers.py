# -*- coding: utf-8 -*-
# from odoo import http


# class GestionUniversités(http.Controller):
#     @http.route('/gestion_universités/gestion_universités/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_universités/gestion_universités/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_universités.listing', {
#             'root': '/gestion_universités/gestion_universités',
#             'objects': http.request.env['gestion_universités.gestion_universités'].search([]),
#         })

#     @http.route('/gestion_universités/gestion_universités/objects/<model("gestion_universités.gestion_universités"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_universités.object', {
#             'object': obj
#         })
