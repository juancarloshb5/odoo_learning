# -*- coding: utf-8 -*-

from odoo  import models,fields

class Production(models.Model):
    _name = "ventanas.production"
    _description = "Production Order"

    name = fields.Char("Order Ref")
    price = fields.Float("Price")


# def productionFromPresupuesto(self, presupuesto: Presupuesto) -> Production:
#     production = Production()
#     production.name = presupuesto.name
#     production.price = presupuesto.price
#     return production;
