# -*- coding: utf-8 -*-
{
    'name': "Multi-currency",

    'summary': """
        Specify currency in which products' prices/costs are expressed. Correctly
        show multi-currency pricing in sales orders and automatically update
        MXN to USD exchange rate. """,

    'description': """
    """,

    'author': "Antonio Aguilar",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale_management', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/sale_order_view.xml',
        'views/res_config_settings_view.xml',
        'data/ir_cron.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}