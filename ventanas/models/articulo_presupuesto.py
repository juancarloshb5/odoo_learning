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
    # name = fields.Char(string="Referencia")

    cantidad = fields.Integer(string="Cantidad")
    precio = fields.Float(string="Precio", related="product_id.list_price")

    precio_calculado = fields.Float(string="Precio Calculado")


    @api.onchange('product_id')
    def _change_precio(self):
        for record in self:
            record.precio_calculado = record.product_id.list_price
