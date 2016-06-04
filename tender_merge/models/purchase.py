# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'


    @api.multi
    def button_confirm(self):
        procurement_obj = self.env['procurement.order']
        res = super(PurchaseOrder, self).button_confirm()
        for po in self:
            if po.requisition_id:
                for line in po.order_line:
                    proc = procurement_obj.search([('requisition_id', '=', line.order_id.requisition_id.id), ('product_id', '=', line.product_id.id)])
                    if proc:
                        proc.purchase_line_id = line.id
        return res
                    
                
	        
	




PurchaseOrder()
