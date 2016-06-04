# -*- coding: utf-8 -*-

from openerp import api, fields, models, _

class PurchaseRequisition(models.Model):

	_inherit = 'purchase.requisition'

	merged = fields.Boolean(string="Merged Tender", default=False)

	@api.multi
	def print_requisition_report(self, data):
		return self.env['report'].get_action(self, 'tender_merge.report_tender', data=data)	
	
PurchaseRequisition()
