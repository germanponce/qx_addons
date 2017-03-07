# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_concepto_rebate_f(models.Model):
	_name= 'autos.catalogo.concepto.rebate.f'
	_description='Conceptos de Rebate'
	rec_name = 'descripcion'
	descripcion = fields.Char('Descripcion',size=100,reqired=True,readonly=False, help='Descripcion Rebate')
	tipo_rebate = fields.Many2one('autos.catalogo.tipo.rebate','Tipo Rebate')
	cliente = fields.Many2one('res.partner','Cliente')
	cartera = fields.Many2one('autos.catalogo.tipo.rebate','Cartera')
	proveedor = fields.Many2one('account.invoice','Proveedor')

