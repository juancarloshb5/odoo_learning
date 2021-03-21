# -*- coding: utf-8 -*-
from odoo import models,fields,api

class ventana(models.Model):
    _name = "ventanas.ventana"
    _description = "modelo de ventana"
    name = fields.Char("Nombre")
    ubicacion = fields.Char("ubicacion")
    precio = fields.Float("Precio")
    medida = fields.Selection([("pulg","Pulgadas"),("mm", "Milimetros")])
    ancho = fields.Integer("Ancho")
    alto = fields.Integer("Alto")
    area = fields.Float("Area", compute="_area_pc", store=True)
    sistema = fields.Many2one("ventanas.sistema", "Sistema", required=False)
    color = fields.Many2one("ventanas.color")
    active = fields.Boolean(default=True)

    _sql_constraints = [(
        'nombre_ventana',
        'unique(name)',
        'This ventana alredy exists'
    )]

    @api.depends('ancho','alto')
    def _area_pc(self):
        self.area = float(self.ancho * self.alto) / 1000000

    def desactivar(self):
        self.active = False


class Sistema(models.Model):
    _name ="ventanas.sistema"
    _description = "Sistemas"

    name= fields.Char("Codigo")
    description = fields.Char("Descripcion")

class Color(models.Model):
    _name = "ventanas.color"
    _description = "Color de acabado"

    name = fields.Char("Color")