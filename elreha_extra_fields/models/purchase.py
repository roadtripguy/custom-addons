from openerp import api, fields, models, _



class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    delivery_id = fields.Many2one('delivery.carrier','Ship Via')
