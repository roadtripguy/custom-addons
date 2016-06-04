# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime, timedelta
from openerp import SUPERUSER_ID
from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError
from openerp.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT



class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    
    blanket_order = fields.Boolean("Blanket Order")
    
 
    
    
class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'
    
    qty_contract = fields.Integer("Contract Qty")
    # compute='_compute_total'

