from odoo import models, fields, api

class CurrencyProduct(models.Model):
    _inherit = "product.template"

    @api.model
    def _get_default_currency(self):
        res = self.env.ref("base.USD").id
        return res

    currency_price = fields.Many2one(comodel_name="res.currency", string="Moneda", required=True, default=_get_default_currency)

    
