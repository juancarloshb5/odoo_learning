from odoo import fields, models, api

class ModeloEtapa(models.Model):
    _name="proyectos.modelo_etapa"
    _description="Modelo Etapa"

    name= fields.Char(string="Id")
    etapa = fields.Many2one(comodel_name="proyectos.etapa", readonly=True)
    proyecto = fields.Many2one(related="etapa.proyecto")
    modelo = fields.Many2one(comodel_name="proyectos.proyecto_modelo",default=1, domain="[('proyecto_id','=',proyecto)]")
    cantidad = fields.Integer(string="Cantidad", default=1)
    ancho = fields.Integer(string="Ancho(mm)")
    alto = fields.Integer(string="Alto(mm)")
    precio = fields.Float(string="Precio")
    precio_presupuesto = fields.Float(string="Precio Presupuesto", readonly=True, related="modelo.precio")
    subtotal_presupuesto = fields.Float(string="Subtotal Presupuesto", compute="_subtotal_presupuesto", store=True)
    subtotal_ejecutado = fields.Float(string="Subtotal Ejecutado", compute="_subtotal_ejecutado", store=True)

    @api.depends('cantidad', 'modelo')
    def _subtotal_presupuesto(self):
        for modelo in self:
            modelo.subtotal_presupuesto = modelo.cantidad * self.modelo.precio

    @api.depends('cantidad','precio')
    def _subtotal_ejecutado(self):
        for modelo in self:
            modelo.subtotal_ejecutado = self.cantidad * self.precio

    # @api.depends('etapa')
    # def _proyecto(self):
    #     if(self.etapa != None):
    #         self.proyecto = self.etapa.proyecto
    #     else:
    #         self.proyecto = -1