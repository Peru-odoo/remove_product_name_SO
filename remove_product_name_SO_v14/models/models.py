# -*- coding: utf-8 -*-

from odoo import models, fields, api, osv


class _RemoveNameFromDesc(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(_RemoveNameFromDesc, self).product_id_change()
        self.name = self.product_id.description_sale if self.product_id and self.product_id.description_sale else self.product_id.name
        return res