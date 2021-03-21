from odoo import  models, fields

class Articulo(models.Model):
    _inherit = 'product.template'
    x_codigo = fields.Char(string="Codigo")