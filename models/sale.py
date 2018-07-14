# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017 Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from openerp import api, models, fields

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'

    last_price1 = fields.Float('Last Sale Price 1', help="Shows the last sales price of the product for selected customer from the Past two Sales order")
    last_price2 = fields.Float('Last Sale Price 2', help="Shows the second last sales price of the product for selected customer from the Past two Sales order")

    #For update the onchange of product
    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        result = {}
        last_price1 = 0.0
        last_price2 = 0.0
        res = super(sale_order_line, self).product_id_change(cr, uid, ids, pricelist, product, qty=qty,
            uom=uom, qty_uos=qty_uos, uos=uos, name=name, partner_id=partner_id,
            lang=lang, update_tax=update_tax, date_order=date_order, packaging=packaging, fiscal_position=fiscal_position, flag=flag, context=context)
        if res.get('value',False):
            result = res['value']
        line_ids = []
        if product:
            order_lines = self.pool.get('sale.order.line').search(cr, uid, [('order_partner_id', '=', partner_id),('product_id', '=', product),('order_id.state','=','done')], context=context)
            if order_lines:
                for lines in order_lines:
                    line_ids.append(lines)
        final_list = sorted(line_ids, key=int, reverse=True)
        if len(final_list)>=1:
            last_price1 = self.pool.get('sale.order.line').browse(cr, uid, final_list[0], context=context).price_unit
            result['last_price1'] = last_price1
        if len(final_list)>=2:
            last_price2 = self.pool.get('sale.order.line').browse(cr, uid, final_list[1], context=context).price_unit
            result['last_price2'] = last_price2
        return {'value': result}

