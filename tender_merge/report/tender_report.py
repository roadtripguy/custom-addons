# -*- coding: utf-8 -*-

import time
from openerp import api, models, _


class TenderReport(models.AbstractModel):

    _name = 'report.tender_merge.report_tender'

    @api.multi
    def _get_po_line_per_product(self, tender, product_id):
        result = []
        if tender and product_id:
            for po in tender.purchase_ids:
                if po.state not in ['cancel']:
                    for po_line in po.order_line:
                        if po_line.product_id.id == product_id.id:
                            result.append(po_line)
        return result 

    @api.multi
    def _get_value(self, purhase_order_lines):
        qty = 0
        total = 0
        per_unit = 0
        for line in purhase_order_lines:
            qty += line.product_qty 
            total += line.price_subtotal 
        if total:
            per_unit = total/qty
        return {'total_qty':qty, 'total':total, 'per_unit':per_unit}

    @api.multi
    def _get_source(self,origin):
        if origin and ':' in origin:
            return origin.split(':')[0]
        else:
            return origin

    @api.multi
    def render_html(self, data):

        model = self.env['report']._get_report_from_name('tender_merge.report_tender').model

        docargs = {
        'doc_ids': self.ids,
        'doc_model': model,
        'data': data,
        'docs': self.env[model].browse(self.ids),
        'time': time,
        'get_value':self._get_value,
        'get_source':self._get_source,
        'get_po_line_per_product':self._get_po_line_per_product
        }

        return self.env['report'].render('tender_merge.report_tender', values=docargs)