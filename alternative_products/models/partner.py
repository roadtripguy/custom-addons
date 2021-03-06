# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _



class Partner(models.Model):
    """Partner inherited """

    _inherit ='res.partner'


    is_manufacturer=fields.Boolean("Is Manufacturer")


class Alternate_manufacturer(models.Model):
    """Alternate manufacturers """

    _name ='alternate.manufacturer'
    _description = 'Alternate Manufacturers on Products'

    manufacturer_id = fields.Many2one('product.template', "Products")
    partner_id = fields.Many2one('res.partner', "Manufacturer")
    name = fields.Char("Name")


    @api.model
    def create(self, vals):
        partner_obj = self.env['res.partner']
        if vals.get('partner_id', False) :
            partner = partner_obj.browse(vals.get('partner_id',False))
            vals.update({ 'name':partner.name or ''

            })


        return super(Alternate_manufacturer, self).create(vals)

    @api.onchange('partner_id')
    def chage_name(self):
        if self.partner_id:
            self.name = self.partner_id.name
