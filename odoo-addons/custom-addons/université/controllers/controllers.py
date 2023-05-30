# -*- coding: utf-8 -*-
# from odoo import http


# class Université(http.Controller):
#     @http.route('/université/université/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/université/université/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('université.listing', {
#             'root': '/université/université',
#             'objects': http.request.env['université.université'].search([]),
#         })

#     @http.route('/université/université/objects/<model("université.université"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('université.object', {
#             'object': obj
#         })
