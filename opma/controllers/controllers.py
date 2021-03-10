# -*- coding: utf-8 -*-
# from odoo import http


# class Opma(http.Controller):
#     @http.route('/opma/opma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/opma/opma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('opma.listing', {
#             'root': '/opma/opma',
#             'objects': http.request.env['opma.opma'].search([]),
#         })

#     @http.route('/opma/opma/objects/<model("opma.opma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('opma.object', {
#             'object': obj
#         })
