# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time

from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError

class GenerateSaleLines(models.TransientModel):
    _name ="generate.salelines"
    
    sale_line_id = fields.Many2one('sale.order.line' , domain=[('product_uom_qty', '=', 0)])
    quantity = fields.Integer("Qunatity")

    @api.multi
    def generate_lines(self):
        for line in self :
            line.sale_line_id.copy({ 'order_id' : line.sale_line_id.order_id.id,'product_uom_qty': self.quantity, 'qty_contract':0})
            line.sale_line_id.write({'qty_contract':line.sale_line_id.qty_contract - self.quantity })





