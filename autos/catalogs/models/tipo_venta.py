#-*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_venta(models.Model):
	_name= 'autos.catalogo.tipo.venta'
	_description='Tipos de Venta'
	_rec_name = 'descripcion'

	descripcion = fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion del Tipo de Venta')
	ventaespecial = fields.Boolean('Venta Especial', required=False)
	cuenta = fields.Many2one('account.account','Cuenta',required = False, help='Cuenta contable del Tipo de Venta')
	active = fields.Boolean('Activo', required = True,default=True)
