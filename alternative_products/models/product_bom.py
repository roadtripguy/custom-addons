# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _
from openerp.osv import osv


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

    #


    def onchange_product_id(self, cr, uid, ids, product_id, product_qty=0, context=None):
        """ Changes UoM if product_id changes.
        @param product_id: Changed product_id
        @return:  Dictionary of changed values
        """
        res = super (ProductsBOM, self).onchange_product_id(cr, uid, ids,product_id)
        if product_id:
            prod = self.pool.get('product.product').browse(cr, uid, product_id)
            al_product_ids =  [product.id for product in prod.alternative_products]
            res.update({'domain':{
                             'alternate_products':[('id', 'in',al_product_ids)]
                                 }
                        })

        return res
