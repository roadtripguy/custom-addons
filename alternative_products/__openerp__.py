# -*- coding: utf-8 -*-
{
    'name': "alternate_product",

    'summary': """
        Module Manage the Alternative products  """,

    'description': """
          Module Manage the Alternative products
    """,

    'author': "SarathKumar",
    'website': "http://www.elrehac.com",
    'category': 'sales',
    'version': '0.2',

    'depends': ['base','sale','mrp'],

    'data': [
          'security/ir.model.access.csv',
         'views/product_view.xml',
         'views/product_bom_view.xml',
         'views/partner_view.xml'

    ],
    'demo': [
    ],
}
