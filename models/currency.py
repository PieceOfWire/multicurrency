import requests
import math
from odoo import api, models, fields
from odoo.exceptions import Warning
from datetime import datetime, timedelta

API_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/"

class MultiCurrency(models.Model):
    _inherit = "res.currency"

    def get_banxico_mxn_usd_rate(self):
        val = self.env["ir.config_parameter"].sudo()
        bmx_token_banxico = val.get_param("multicurrency.bmx_token")

        date = datetime.today()
        if date.weekday() == 0: # On monday use exchange rate from friday
            date -= timedelta(3)
        elif date.weekday() == 5 or date.weekday() == 6: # Exchange rate not updated on weekends.
            return -1
        else:
            date -= timedelta(1)
            
        date = date.strftime(r"%Y-%m-%d")
        req_url = API_URL + date + "/" + date
        bmx_header = {"Bmx-Token": bmx_token_banxico}
        response = requests.get(req_url, headers=bmx_header)
        if response.status_code != 200:
            raise Exception("Status code " + str(response.status_code))
        return 1 / float(response.json()["bmx"]["series"][0]["datos"][0]["dato"])

    @api.model
    def update_mxn_usd_rate(self):
        try:
            rate = self.get_banxico_mxn_usd_rate()
            if rate == -1: # Weekday. Rates are not updated
                return
            # Truncate to 6 decimal places
            rate = math.trunc(rate * (10.0 ** 6)) / (10.0 ** 6)
            date = fields.Date.today()
            currency_id = self.env.ref("base.USD").id
            rate_obj = self.env["res.currency.rate"]
            current_rate = rate_obj.search([("currency_id", "=", currency_id), ("name", "=", date)])
            if not current_rate:
                rate_obj.create({
                    "name": date,
                    "rate": rate,
                    "currency_id": currency_id,
                    "company_id": self.env.user.company_id.id
                })
            else:
                current_rate.write({"rate": rate})
            self.env.cr.commit()
        except Exception as ex:
            raise Warning(str(ex))