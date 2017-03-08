# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api,exceptions
import odoo.addons.decimal_precision as dp


class product_template(models.Model):
    _inherit = 'product.template'

    is_car = fields.Boolean('Es Automovil?')

    type_car = fields.Selection([
                                ('new','Auto Nuevo'),
                                ('used','Auto Usado'),
                                ], 'Tipo de Automovil')

    accesorios_ids = fields.Many2many('autos.catalogo.accesorios',
                                        'product_accesorios_rel','product_id','accesorio_id', 'Accesorios')

class autos_catalogo_accesorios(models.Model):
    _inherit = 'autos.catalogo.accesorios'

    product_ids = fields.Many2many('product.template',
                                        'product_accesorios_rel','accesorio_id','product_id', 'Productos')
