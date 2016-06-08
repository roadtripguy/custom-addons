# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time

from openerp import api, fields, models, _
import openerp.addons.decimal_precision as dp
from openerp.exceptions import UserError

class GenerateSaleLines(models.TransientModel):
    _name ="generate.salelines"

    @api.model
    def get_order(self):
        return self._context.get('active_ids')[0]

    @api.onchange('sale_id')
    def on_change_sale_id(self):
        return {'domain':{ 'sale_line_id':[('order_id','=', self.sale_id.id),('product_uom_qty','=',0)]}}

    sale_id = fields.Many2one('sale.order',string = 'Sale Order', default = get_order)
    sale_line_id = fields.Many2one('sale.order.line' ,string ='Contract Line', domain=[('product_uom_qty', '=', 0)])
    quantity = fields.Integer("Quantity")

    @api.multi
    def generate_lines(self):
        for line in self :
            if not line.quantity :
               raise UserError(_('Please enter a valid quantity'))
            if line.quantity > line.sale_line_id.qty_contract :
                raise UserError(_('You cannot release quantity reater than in contract'))
            line.sale_line_id.copy({ 'order_id' : line.sale_line_id.order_id.id,'product_uom_qty': line.quantity, 'qty_contract':0})
            line.sale_line_id.write({'qty_contract':line.sale_line_id.qty_contract - self.quantity })


