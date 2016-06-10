# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import api, fields, models, _


class Bomline(models.Model):
    _inherit = 'mrp.bom.line'

    reference_designators = fields.Text("Reference Designators(CSV)")
    elreha_item_number =  fields.Char("Elreha Item #")