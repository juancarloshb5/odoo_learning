from odoo import fields, models, api

class ModeloEtapa(models.Model):
    _name="proyectos.modelo_etapa"
    _description="Modelo Etapa"

    name= fields.Char(string="Referencia")
    etapa = fields.Many2one(comodel_name="proyectos.etapa")

    proyecto_id = fields.Many2one(related="etapa.proyecto_id", readonly=True)
    modelo_id = fields.Many2one(comodel_name="proyectos.proyecto_modelo", domain="[('proyecto_id','=',proyecto_id)]")
    cantidad = fields.Integer(string="Cantidad", default=1)
    ancho = fields.Integer(string="Ancho(mm)")
    alto = fields.Integer(string="Alto(mm)")
    precio = fields.Float(string="Precio")
    precio_presupuesto = fields.Float(string="Precio Presupuesto", readonly=True, related="modelo_id.precio")
    subtotal_presupuesto = fields.Float(string="Subtotal Presupuesto", compute="_subtotal_presupuesto", store=True)
    subtotal_ejecutado = fields.Float(string="Subtotal Ejecutado", compute="_subtotal_ejecutado", store=True)

    @api.depends('cantidad', 'modelo_id')
    def _subtotal_presupuesto(self):
        for modelo in self:
            modelo.subtotal_presupuesto = modelo.cantidad * modelo.modelo_id.precio

    @api.depends('cantidad','precio')
    def _subtotal_ejecutado(self):
        for modelo in self:
            modelo.subtotal_ejecutado = modelo.cantidad * modelo.precio

    # @api.depends('etapa')
    # def _proyecto(self):
    #     if(self.etapa != None):
    #         self.proyecto = self.etapa.proyecto
    #     else:
    #         self.proyecto = -1