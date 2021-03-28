

from odoo.odoo import models


class Defaults:
    @staticmethod
    def default_currency():
        # return models.Model.env['res.currency'].search([('name','=','DOP')],limit=1).id
        return 74
