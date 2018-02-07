# -*- coding: utf-8 -*-

from openerp import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    project_id = fields.Many2one(
        'project.project',
        string='Project')

    @api.onchange('project_id')
    def _onchange_project_id(self):
        stock_picking_type = self.env['stock.picking.type']
        domain = ['|', ('name', 'ilike', self.project_id.name),
                  ('name', 'ilike', self.project_id.code),
                  ('code', '=', 'incoming')]
        picking_type_id = stock_picking_type.search(domain)
        self.picking_type_id = picking_type_id.id
