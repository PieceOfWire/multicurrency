from odoo import models, fields, api
from odoo.exceptions import Warning

class CurrencySaleOrder(models.Model):
    _inherit = "sale.order"    

    def calc_currency_price(self):
        for record in self:
            currency = record.pricelist_id.currency_id
            for line in record.order_line:
                if line.display_currency != currency and line.display_currency:
                    line_rate = line.display_currency.rate
                    line.price_unit /= line_rate
                    line.purchase_price /= line_rate
                    line.display_currency = currency
           

class CurrencySaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    display_currency = fields.Many2one(comodel_name="res.currency", string="Moneda", required=True)

    @api.onchange("product_id")
    def display_product_price(self):
        for line in self:
            line.price_unit = line.product_id.list_price
            line.price_unit = line.product_id.standard_price
            line.display_currency = line.product_id.currency_price
