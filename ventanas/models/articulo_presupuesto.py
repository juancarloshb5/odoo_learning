# -*- coding: utf-8 -*-

from odoo import  models, fields, api

class ArticuloPresupuesto(models.Model):
    _name = "ventanas.articulo.presupuesto"
    _description = "Articulos Presupuestos"

    presupuesto_id = fields.Many2one(
        comodel_name="ventanas.presupuesto",
        string="Presupuesto"
    )

    product_id = fields.Many2one(
        comodel_name="product.template",
        string="Articulo"
    )
    name = fields.Char(string="Referencia", related="product_id.name")
    quantity = fields.Integer(string="Cantidad")
    price = fields.Float(string="Precio")
    subtotal = fields.Float(string="Subtotal", compute="_subtotal", store=True)

    @api.onchange('product_id')
    def _change_precio(self):
        for record in self:
            record.price = record.product_id.list_price

    @api.depends('quantity','price')
    def _subtotal(self):
        for articulo in self:
            articulo.subtotal = float(articulo.quantity) * articulo.price
