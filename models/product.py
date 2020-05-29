from odoo import models, fields, api

class CurrencyProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def _get_default_currency(self):
        res = self.env.ref("base.USD").id
        return res

    currency_price = fields.Many2one(comodel_name="res.currency", string="Moneda", required=True, default=_get_default_currency)

class CurrencyProductProduct(models.Model):
    _inherit = "product.product"

    currency_price = fields.Many2one(comodel_name="res.currency", string="Moneda", related="product_tmpl_id.currency_price")

    
