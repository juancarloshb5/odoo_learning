from odoo import  models, fields

class Articulo(models.Model):
    _inherit = 'product.template'
    x_codigo = fields.Char(string="Codigo")

    _sql_constraints = [(
        'unique_codigo_articulo',
        'unique(x_codigo)',
        'Esta codigo ya existe en la base de datos'
    )]