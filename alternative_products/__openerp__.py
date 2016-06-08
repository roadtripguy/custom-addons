# -*- coding: utf-8 -*-
{
    'name': "alternate_product",

    'summary': """
        Module Manage the Alternative products  """,

    'description': """
          Module Manage the Alternative products
    """,

    'author': "SarathKumar",
    'website': "http://www.yourcompany.com",
    'category': 'sales',
    'version': '0.1',

    'depends': ['base','sale','mrp'],

    'data': [
          'security/ir.model.access.csv',
         'views/product_view.xml',
         'views/product_bom_view.xml'

    ],
    'demo': [
    ],
}
