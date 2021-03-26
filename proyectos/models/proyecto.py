from odoo import  models, fields, api


class Proyecto(models.Model):
    _name = "opma.proyecto"
    _description = "Proyectos"

    name = fields.Char(string = "Obra", required= True)
    active = fields.Boolean(string="Activo" , default = True)
    state = fields.Selection([("proceso","En Proceso"), ("aprobado","Aprobado"), ("descartado","Descartado")])
    cliente = fields.Many2one(string="Cliente", comodel_name="res.partner", required=True)
    presupuesto_winperfil = fields.Char(string="Presupuesto Winperfil")
    precio_venta = fields.Monetary(string="Precio Venta")
    currency_id = fields.Many2one("res.currency", string="Moneda")
    precio_instalacion = fields.Monetary(string="Precio Instalacion")










