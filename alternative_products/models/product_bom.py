# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _



class Bom_Alternate_products(models.Model):
    '''Alternate Products on Bom line
    '''
    _name = 'bom.alternate.prodcts'
    _description = 'Alternate Products on BoM line'

    product_id = fields.Many2one('product.template', 'Product Name' )
    alternate_product_id = fields.Many2one('product.template', 'Product Name' )
    bom_line_id = fields.Many2one('mrp.bom.line', 'BOM Line')
    name = fields.Char('Name')


    @api.onchange('product_id')
    def chage_name(self):
        if self.product_id:
            self.name = self.product_id.name


class ProductsBOM(models.Model):
    """Alternate products """
    _inherit ='mrp.bom.line'


    alternate_products =  fields.Many2many('bom.alternate.prodcts', string = 'Alternate Products')
    alternate_manufacturers =  fields.Many2many('res.partner', string = 'Alternate Manufacturers')
    
    
