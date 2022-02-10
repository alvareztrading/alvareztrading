# -*- coding: utf-8 -*-


from odoo import models, fields, api,_
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class SaleOrderInh(models.Model):
    _inherit = "sale.order.line"

    weight = fields.Float(string="Weight")

    @api.onchange('product_id')
    def _onchange_fill_weight(self):
        for record in self:
            record.weight = record.product_id.weight


