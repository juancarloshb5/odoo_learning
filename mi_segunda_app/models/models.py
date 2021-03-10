# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class mi_segunda_app(models.Model):
#     _name = 'mi_segunda_app.mi_segunda_app'
#     _description = 'mi_segunda_app.mi_segunda_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
