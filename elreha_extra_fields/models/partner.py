# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _



class Partner(models.Model):
    _inherit = 'res.partner'

    reseller_id = fields.Char("Reseller ID")
