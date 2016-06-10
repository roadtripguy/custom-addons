# -*- coding: utf-8 -*-
from openerp import models, api, _
from openerp.exceptions import UserError


class TenderMergeConfirm(models.TransientModel):
    """
    This wizard will merge the all the selected tenders
    """

    _name = "tender.merge"
    _description = "Merge the selected tenders"

    @api.multi
    def merge_confirm(self):

        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        tenders = self.env['purchase.requisition'].browse(active_ids)

        if tenders:

            if len(tenders) < 2:
                raise UserError('Warning \n Select Multiple Tenders to Merge')            
            if 'cancel' in tenders.mapped('state'):
                raise UserError('Warning \n Cannot merge tenders marked canceled')

            requisition_line_ids = tenders.mapped('line_ids')
            purchase_ids = tenders.mapped('purchase_ids')
            procurement_ids = tenders.mapped('procurement_id')
            print procurement_ids,procurement_ids.mapped('group_id')
            if len(procurement_ids.mapped('group_id')) != 1:
                raise UserError('Warning \n Cannot merge tenders with different sources')
            if any(tenders.mapped('merged')):
                raise UserError('Warning \n Merge not possible with already merged tenders ')
                
            origin = []
            for value in tenders.mapped('origin'):
                if value == False:
                    continue
                origin.append(value)

            if origin:
                if ':' in origin[0]:
                    source = origin[0].split(':')[0]
                else:
                    source = origin[0]
            else:
                source = ''
            new_tender = self.env['purchase.requisition'].create({'origin' : source, 'merged':True})
            tenders.write({'state':'cancel'})

            if new_tender:
                requisition_line_ids.write({'requisition_id' : new_tender.id})
                purchase_ids.write({'requisition_id' : new_tender.id, 'origin' : new_tender.name})
                procurement_ids.write({'requisition_id' : new_tender.id})
                for tender in tenders:
                    tender.message_post(body=_('Requisition cancelled and merged to %s'%(new_tender.name)))

        return {'type': 'ir.actions.act_window_close'}      