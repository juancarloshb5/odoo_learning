
import requests
import json

from odoo import  models, fields, api, exceptions
from datetime import  date
from ..helpers.defaults import Defaults

class Proyecto(models.Model):
    @api.depends('modelos')
    def _calculo_presupuesto(self):
        subtotal = 0
        for modelo in self.modelos:
            subtotal += modelo.cantidad * modelo.precio
        self.precio_presupuestado = subtotal

    @api.depends('etapas')
    def _calculo_ejecutado(self):
        subtotal = 0
        for etapa in self.etapas:
            subtotal += etapa.precio_ejecutado
        self.precio_ejecutado = subtotal

    @api.depends('etapas')
    def _calculo_ejecutado_presupuesto(self):
        subtotal = 0
        for etapa in self.etapas:
            subtotal += etapa.precio_presupuesto
        self.precio_ejecutado_presupuesto = subtotal


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
    fecha_terminado = fields.Date(string="Fecha Terminado")
    presupuesto_adjunto = fields.Binary(string="Presupuesto")

    precio_presupuestado = fields.Float(string="Presupuesto Total", compute="_calculo_presupuesto")
    precio_ejecutado = fields.Float(string="Ejecutado", compute="_calculo_ejecutado")
    precio_ejecutado_presupuesto = fields.Float(string="Ejecutado Presupuesto", compute="_calculo_ejecutado_presupuesto")

    modelos = fields.One2many(comodel_name="proyectos.proyecto_modelo", inverse_name="proyecto_id")
    etapas = fields.One2many(comodel_name="proyectos.etapas", inverse_name="proyecto_id")




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

    def post_proyecto(self):
        print("Posting")
        proyecto = json.dumps({
            'id': 10,
            'cliente': 'self.cliente.id'
        })
        r = requests.post('http://localhost:56503/api/Odoo/Proyecto',json={'id':self.id}, params={"id": self.id})
        print(r.status_code)
        if (r.status_code == requests.codes.ok):
            print("Get Value")
        else:
            print("Bad")

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
















