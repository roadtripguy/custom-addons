# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _




class Product(models.Model):
    _inherit = 'product.template'
    alias_ids = fields.One2many("product.alias",'product_id')

Product()

class ProductAlias(models.Model):
    _name = 'product.alias'
    _description = "Product Aliases "
    name = fields.Char('Name')
    product_id = fields.Many2one('product.template') 

ProductAlias()




    
