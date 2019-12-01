# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import Warning


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    barcode = fields.Char(string='Barcode')
    serial_num=fields.Char('Serial No.')

class StockPickingOperation(models.Model):
    _inherit = 'stock.move'

    barcode = fields.Char(string='Barcode')

    @api.onchange('barcode')
    def _onchange_barcode_scan(self):
        product_rec = self.env['product.product']
        if self.barcode:
            product = product_rec.search([('barcode', '=', self.barcode)])
            self.product_id = product.id

