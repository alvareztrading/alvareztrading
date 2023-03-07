# -*- coding: utf-8 -*-


from odoo import models, fields, api,_
from datetime import datetime
from odoo.exceptions import ValidationError , UserError
from datetime import date
from dateutil.relativedelta import relativedelta


class ProductProductInh(models.Model):
    _inherit = "product.template"

    company_wise_ids = fields.Many2many('res.company')


class SaleOrderLineInh(models.Model):
    _inherit = "sale.order.line"

    weight = fields.Float(string="Total Weight", compute='_compute_weight')

    def _compute_weight(self):
        for record in self:
            record.weight = record.product_id.weight * record.product_uom_qty


class SaleOrderInh(models.Model):
    _inherit = "sale.order"

    total_weight = fields.Float(string="Weight Sub Total", compute='_compute_total_weight')

    active = fields.Boolean(string='Active', defualt=True)

    @api.model
    def create(self, vals):
        vals['active'] = True,
        rec = super(SaleOrderInh, self).create(vals)
        return rec

    def _compute_total_weight(self):
        t_w = 0
        for record in self.order_line:
            t_w = t_w + record.weight
        self.total_weight = t_w


class PickingInh(models.Model):
    _inherit = "stock.picking"

    active = fields.Boolean(string='Active', default=True)

    @api.model
    def create(self, vals):
        vals['active'] = True,
        rec = super(PickingInh, self).create(vals)
        return rec


class PurchaseInh(models.Model):
    _inherit = "purchase.order"

    active = fields.Boolean(string='Active', default=True)

    @api.model
    def create(self, vals):
        vals['active'] = True,
        rec = super(PurchaseInh, self).create(vals)
        return rec


class StockLotInh(models.Model):
    _inherit = "stock.production.lot"

    @api.onchange('expiration_date')
    def change_expiration_date(self):
        for rec in self:
            if rec.expiration_date:
                rec.alert_date = rec.expiration_date - relativedelta(months=9)
