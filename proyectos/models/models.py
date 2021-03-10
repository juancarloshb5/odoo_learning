# -*- coding: utf-8 -*-

from odoo import models, fields, api


class proyecto(models.Model):
    _name = 'proyectos.proyecto'
    _description = 'Proyecto'

    codigo = fields.Integer()
    nombre = fields.Char("Nombre del proyecto")
    contacto = fields.Char(string="Contacto")
