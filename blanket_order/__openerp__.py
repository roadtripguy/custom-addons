# -*- coding: utf-8 -*-
{
    'name': "blanket_order",

    'summary': """
        Module to process the blanket orders using odoo  """,

    'description': """
         Module to process the blanket orders using odoo
    """,

    'author': "SarathKumar",
    'website': "http://www.elrehac.com",
    'category': 'sales',
    'version': '0.2',

    'depends': ['base','sale'],

    'data': ['wizard/generate_lines_view.xml',
        'views/sale_view.xml',

    ],
    'demo': [
    ],
}
