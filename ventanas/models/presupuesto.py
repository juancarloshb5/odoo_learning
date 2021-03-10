# -*- coding: utf-8 -*-
from odoo  import models, fields


class Presupuesto(models.Model):
    _name = "ventanas.presupuesto"
    _description = "Presupuesto de Ventanas"

    name = fields.Char("Referencia")
    price = fields.Float("Price")
    active = fields.Boolean("Activo")
    state = fields.Selection([("proceso","En Proceso"), ("aprobado","Aprobado"), ("cancelado","Cancelado")])
    customer = fields.Many2one(
        comodel_name="res.partner",
        domain="[('is_company', '=', True)]",
        required= True

    )
    articulos = fields.One2many(
        comodel_name="ventanas.articulo.presupuesto",
        inverse_name="presupuesto_id",
        string="Articulos"
    )

    def approve(self):
        self.state = "aprobado"
        production = self.env['ventanas.production'].create({'name': self.name, "price": self.price})
        self.env.cr.commit()



