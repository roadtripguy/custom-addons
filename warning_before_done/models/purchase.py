# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit ='purchase.order'

    @api.multi
    def action_back_purchase(self):
        self.ensure_one()
        self.write({'state':'purchase'})
