# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models, _

class SaleOrder(models.Model):
    _inherit ='sale.order'

    @api.multi
    def action_back_sale(self):
        self.ensure_one()
        self.write({'state':'sale'})
