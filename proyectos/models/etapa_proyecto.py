from odoo import models, api, fields
from ..helpers.defaults import Defaults

class Etapa(models.Model):
    _name = "proyectos.etapa"
    _description="Etapa de un proyecto"

    name = fields.Char(string="Nombre Etapa")

    proyecto_id = fields.Many2one(comodel_name="proyectos.proyecto")
    proyecto_context = fields.Integer(string="Proyecto Context")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Moneda", default=Defaults.default_currency())
    fecha_inicio = fields.Date("Fecha Inicio")
    presupuesto_winperfil = fields.Integer("Presupuesto Winperfil")
    oferta_winperfil = fields.Integer("Oferta Winperfil")
    presupuesto_adjunto = fields.Binary("Presupuesto Adjunto")
    state = fields.Selection(
        [
            ('registro',"En proceso de registro"),
            ('proceso',"En Produccion"),
            ('instalacion',"Instalando"),
            ('terminada',"Terminada"),
            ('recibida',"Recibida"),
        ], default="registro", string="Estado")
    instalacion_calculada = fields.Monetary(string="Instalacion Calculada", readonly=True)
    instalacion_pagar = fields.Monetary(string="Instalacion a pagar")
    precio_ejecutado = fields.Monetary(string="Precio Calculado", readonly=True, compute="_calculo_precio_ejecutado", store=True)
    precio_presupuesto = fields.Monetary(string="Precio Winperfil", readonly=True, compute="_calculo_precio_presupuesto", store=True)
    modelos = fields.One2many(comodel_name="proyectos.modelo_etapa", inverse_name="etapa")


    @api.depends('modelos')
    def _calculo_precio_ejecutado(self):
        for etapa in self:
            subtotal = 0
            for modelo in etapa.modelos:
                subtotal += modelo.subtotal_ejecutado
            etapa.precio_ejecutado= subtotal

    @api.depends('modelos')
    def _calculo_precio_presupuesto(self):
        for etapa in self:
            subtotal = 0
            for modelo in etapa.modelos:
                subtotal += modelo.subtotal_presupuesto
            etapa.precio_presupuesto = subtotal




