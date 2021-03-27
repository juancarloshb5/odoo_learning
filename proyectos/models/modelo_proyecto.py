from odoo import  models, fields, api

class ModeloProyecto(models.Model):
    _name = "opma.proyecto_modelo"
    _description = "Modelo Proyecto"

    proyecto_id = fields.Many2one(comodel_name="opma.proyecto", readonly=True)
    producto_id = fields.Many2one(comodel_name="product.template", domain="[('categ_id','=',4)]")
    name = fields.Char(string="Nombre")
    ancho = fields.Integer(string="Ancho(mm)")
    alto = fields.Integer(string="Alto(mm)")
    cantidad = fields.Integer(string="Cantidad", default=1)
    precio = fields.Float(string="Precio")
    subtotal = fields.Float(string="Subtotal", compute="_subtotal", store=True)






    @api.depends('cantidad', 'precio')
    def _subtotal(self):
        for modelo in self:
            modelo.subtotal = modelo.cantidad * modelo.precio