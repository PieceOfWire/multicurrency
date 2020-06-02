from odoo import models, fields, api
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

# Currently not being used. purchase.order.line seems to be overriding the 
# desired behavior coded here and I am too scared to change or override
# original code.

# class CurrencyPurchaseOrder(models.Model):
#     _inherit = "purchase.order"    

#     def calc_currency_price(self):
#         for record in self:
#             currency = record.currency_id
#             for line in record.order_line:
#                 if line.display_currency != currency and line.display_currency:
#                     line_rate = line.display_currency.rate
#                     conversion_rate = (currency.rate / line_rate)
#                     line.price_unit *= conversion_rate
#                     line.display_currency = currency

#     @api.model
#     def create(self, vals):
#         self.calc_currency_price()
#         return super(CurrencyPurchaseOrder, self).create(vals)

#     @api.multi
#     def write(self, vals):
#         res = super(CurrencyPurchaseOrder, self).write(vals)
#         self.calc_currency_price()
#         return res

           
# class CurrencySaleOrderLine(models.Model):
#     _inherit = "purchase.order.line"

#     display_currency = fields.Many2one(comodel_name="res.currency", string="Moneda", required=True)

#     @api.onchange("product_id")
#     def display_product_price(self):
#         for line in self:
#             line.price_unit = line.product_id.price
#             line.display_currency = line.product_id.currency_price