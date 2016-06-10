# -*- coding: utf-8 -*-
{
    'name': "Extra Elreha Fields ",

    'summary': """
        Extra Fields for Elreha  """,

    'description': """
          Extra Fields for Elreha
    """,

    'author': "SarathKumar",
    'website': "http://www.elrehac.com",
    'category': 'sales',
    'version': '0.2',

    'depends': ['base','sale','mrp'],

    'data': [
         'security/ir.model.access.csv',
         'views/partner_view.xml',
         'views/bom_line_view.xml',
         'views/product_view.xml',


    ],
    'demo': [
    ],
}
