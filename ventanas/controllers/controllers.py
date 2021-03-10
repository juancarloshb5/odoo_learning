# -*- coding: utf-8 -*-
# from odoo import http


# class Ventanas(http.Controller):
#     @http.route('/ventanas/ventanas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ventanas/ventanas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ventanas.listing', {
#             'root': '/ventanas/ventanas',
#             'objects': http.request.env['ventanas.ventanas'].search([]),
#         })

#     @http.route('/ventanas/ventanas/objects/<model("ventanas.ventanas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ventanas.object', {
#             'object': obj
#         })
