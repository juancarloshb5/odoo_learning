# -*- coding: utf-8 -*-

from odoo import  models, fields, api, exceptions

class ArticuloPresupuesto(models.Model):

    @api.constrains('quantity')
    def quantity_validation(self):
        for record in self:
            if (record.quantity <= 0):
                message = "Quantity for {name} must be 1 or more..."
                message = message.format(name=record.name)
                raise exceptions.ValidationError(message)

    @api.onchange('product_id')
    def _change_precio(self):
        for record in self:
            record.price = record.product_id.list_price

    @api.depends('quantity', 'price')
    def _subtotal(self):
        for articulo in self:
            articulo.subtotal = float(articulo.quantity) * articulo.price


    _name = "ventanas.articulo.presupuesto"
    _description = "Articulos Presupuestos"

    presupuesto_id = fields.Many2one(
        comodel_name="ventanas.presupuesto",
        string="Presupuesto",
        readonly=True

    )

    product_id = fields.Many2one(
        comodel_name="product.template",
        string="Articulo"
    )
    name = fields.Char(string="Referencia", related="product_id.name")
    quantity = fields.Integer(string="Cantidad", default=1)
    price = fields.Float(string="Precio")
    subtotal = fields.Float(string="Subtotal", compute="_subtotal", store=True)


    _sql_constraints = [(
                        'unique_articulo_by_presupuesto',
                         'unique(product_id,presupuesto_id)',
                         'Cannot insert duplicate articulos'
                         )]

