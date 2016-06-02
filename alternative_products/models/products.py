# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _



class Products(models.Model):
    """Alternate products """

    _inherit ='product.template'

    alternative_products = fields.One2many('bom.alternate.prodcts', 'alternate_product_id', 'Alternate Products')
