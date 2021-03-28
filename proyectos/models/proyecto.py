from odoo import  models, fields, api, exceptions
from datetime import  date
from ..helpers.defaults import Defaults

class Proyecto(models.Model):
    _name = "proyectos.proyecto"
    _description = "Proyectos"

    name = fields.Char(string = "Obra", required= True)
    active = fields.Boolean(string="Activo" , default = True)
    state = fields.Selection([("proceso","En Proceso"), ("aprobado","Aprobado"), ("terminado","Terminado"), ("descartado","Descartado")], default="proceso")
    cliente = fields.Many2one(string="Cliente", comodel_name="res.partner", required=True)
    presupuesto_winperfil = fields.Char(string="Presupuesto Winperfil")
    numero_presupuesto = fields.Integer(string="Numero Winperfil")
    oferta_presupuesto = fields.Integer(string="Oferta Winperfil")
    precio_venta = fields.Monetary(string="Precio Venta")
    precio_instalacion = fields.Monetary(string="Precio Instalacion")
    # currency_id = fields.Many2one("res.currency", string="Moneda", default=lambda self: self.env['res.currency'].search([('name','=','DOP')],limit=1).id)
    currency_id = fields.Many2one("res.currency", string="Moneda", default=Defaults.default_currency())
    fecha_aprobado = fields.Date(string="Fecha Aprobado", readonly="true")
    presupuesto_adjunto = fields.Binary(string="Presupuesto")

    modelos = fields.One2many(comodel_name="proyectos.proyecto_modelo", inverse_name="proyecto_id")


    def is_manager(self):
        return self.env.user.has_group('proyectos.proyectos_aprobar_proyecto')
        # return True

    def aprobar_proyecto(self):
        if(self.is_manager()):
            for proyecto in self:
                proyecto.state = "aprobado"
                proyecto.fecha_aprobado = date.today()
        else:
            raise exceptions.ValidationError("No tiene privilegios para aprobar")

    def desaprobar_proyecto(self):
        if(self.is_manager()):
            for proyecto in self:
                proyecto.update({
                    'state': "proceso",
                    "fecha_aprobado": None
                })

    def terminar_proyecto(self):
        for proyecto in self:
            proyecto.update({
                'state': "terminado",
            })












