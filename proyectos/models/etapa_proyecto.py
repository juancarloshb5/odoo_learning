from odoo import models, api, fields
from ..helpers.defaults import Defaults

class Etapa(models.Model):
    _name = "proyectos.etapa"
    _description="Etapa de un proyecto"

    name = fields.Char(string="Nombre Etapa")
    proyecto = fields.Many2one(comodel_name="proyectos.proyecto", required=True)
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
        ], default="registro")
    precio_calculado = fields.Monetary(string="Precio Calculado")
    instalacion_calculada = fields.Monetary(string="Instalacion Calculada")
    precio_presupuesto = fields.Monetary(string="Precio Winperfil")
    instalacion_pagar = fields.Monetary(string="Instalacion a pagar")




