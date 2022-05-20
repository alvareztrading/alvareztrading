# -*- coding: utf-8 -*-


from odoo import models, fields, api,_
from datetime import datetime
from odoo.exceptions import ValidationError , UserError


class SaleOrderLineInh(models.Model):
    _inherit = "sale.order.line"

    weight = fields.Float(string="Total Weight", compute='_compute_weight')

    def _compute_weight(self):
        for record in self:
            record.weight = record.product_id.weight * record.product_uom_qty


class SaleOrderInh(models.Model):
    _inherit = "sale.order"

    total_weight = fields.Float(string="Weight Sub Total", compute='_compute_total_weight')

    def _compute_total_weight(self):
        t_w = 0
        for record in self.order_line:
            t_w = t_w + record.weight
        self.total_weight = t_w


