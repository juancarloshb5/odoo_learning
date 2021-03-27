from odoo import  models, fields, api, exceptions


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
    fecha_aprobado = fields.Date(string="Fecha Aprobado")

    modelos = fields.One2many(comodel_name="opma.proyecto_modelo", inverse_name="proyecto_id")


    def is_manager(self):
        return self.env.user.has_group('proyectos.proyectos_aprobar_proyecto')
        # return True

    def aprobar_proyecto(self):
        if(self.is_manager()):
            for proyecto in self:
                proyecto.state = "aprobado"

        else:
            raise exceptions.ValidationError("No tiene privilegios para aprobar")


            # proyecto.fecha_aprobado = fields.Datetime.now









