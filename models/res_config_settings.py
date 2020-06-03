from odoo import fields, models, api
from odoo.exceptions import Warning
import requests
from datetime import datetime, timedelta

# Settings to turn on automatic exchange (MXN to USD) rate from Banxico

class AutomaticCurrency(models.TransientModel):
    _inherit = "res.config.settings"

    banxico_live_currency = fields.Boolean(string="Tipo de cambio de Banxico")
    bmx_token_banxico = fields.Char(string="Token API Banxico", help="Puede ser obtenido de: https://www.banxico.org.mx/SieAPIRest/service/v1/token")
    test_rate = fields.Boolean()
    current_rate = fields.Float(string="Tipo de cambio", digits=(12,7))

    def get_test_rate(self):
        self.test_rate = True
        try:
            self.current_rate = self.env["res.currency"].get_banxico_mxn_usd_rate()
        except Exception as ex:
            raise Warning(str(ex))

    def set_values(self):
        res = super(AutomaticCurrency, self).set_values() 
        self.env["ir.config_parameter"].set_param("multicurrency.banxico_live", self.banxico_live_currency)
        self.env["ir.config_parameter"].set_param("multicurrency.bmx_token", self.bmx_token_banxico)
        return res

    @api.model
    def get_values(self):
        res = super(AutomaticCurrency, self).get_values() 
        val = self.env["ir.config_parameter"].sudo()
        active = val.get_param("multicurrency.banxico_live")
        token = val.get_param("multicurrency.bmx_token")
        res.update(
            banxico_live_currency=active,
            bmx_token_banxico=token
            )
        return res
