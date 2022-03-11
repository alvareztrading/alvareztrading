# -*- coding: utf-8 -*-
{
    'name': "Alvaraiz Custom",

    'summary': """
        This Module Enhance the Functionalities in Alvaraiz""",

    'description': """
        This Module Enhance the Functionalities in Alvaraiz
    """,

    'author': "Viltco",
    'website': "http://www.viltco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '15.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale'],

    # always loaded
    'data': [
        'views/views.xml',
        'reports/sale_template.xml',
        'security/security.xml',
    ],

}
