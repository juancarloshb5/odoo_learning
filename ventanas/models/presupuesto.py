# -*- coding: utf-8 -*-
from odoo  import models, fields, api


class Presupuesto(models.Model):
    _name = "ventanas.presupuesto"
    _description = "Presupuesto de Ventanas"

    name = fields.Char(string="Referencia", required=True)

    active = fields.Boolean(string="Activo", default=True)
    state = fields.Selection([("proceso","En Proceso"), ("aprobado","Aprobado"), ("cancelado","Cancelado")])
    customer = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
        required= True

    )
    street = fields.Char(related="customer.street", string="Calle")
    customer_name = fields.Char(related="customer.name", string="Cliente")
    articulos = fields.One2many(
        comodel_name="ventanas.articulo.presupuesto",
        inverse_name="presupuesto_id",
        string="Articulos"
    )
    facturado = fields.Boolean(string="Facturado")
    price = fields.Float(string="Total", compute="_total_amount", store=True)

    @api.depends('articulos')
    def _total_amount(self):
        for presupuesto in self:
            amount = 0.0
            for articulo in presupuesto.articulos:
                amount += articulo.subtotal
            presupuesto.update({
                'price': amount
            })

    def approve(self):
        self.state = "aprobado"
        production = self.env['ventanas.production'].create({'name': self.name, "price": self.price})
        self.env.cr.commit()



