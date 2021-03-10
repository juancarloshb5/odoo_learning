# -*- coding: utf-8 -*-
# from odoo import http


# class MiSegundaApp(http.Controller):
#     @http.route('/mi_segunda_app/mi_segunda_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mi_segunda_app/mi_segunda_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mi_segunda_app.listing', {
#             'root': '/mi_segunda_app/mi_segunda_app',
#             'objects': http.request.env['mi_segunda_app.mi_segunda_app'].search([]),
#         })

#     @http.route('/mi_segunda_app/mi_segunda_app/objects/<model("mi_segunda_app.mi_segunda_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mi_segunda_app.object', {
#             'object': obj
#         })
