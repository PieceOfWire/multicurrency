# multicurrency
Automatic exchange currency for USD-MX in Odoo. 

A free and open source alternative to Odoo's automatic exchange currency entreprise service. If you need to update MXN-USD exchange dates daily this is for you.

Banxico's API is used to get the official exchange rate and update it in Odoo daily. To use the Banxico API you need to generate a token and add it on Odoo's setting page. You then
have to activate the automatic cron job that updates exchange rates and you are good to go.

Right now there is no menu to add the token to Odoo so you need to add it on the system parameters section. If you have any questions or problems feel free to ask for help. 
