#-*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_almacenes(models.Model):
	_name= 'autos.catalogo.almacenes'
	_description='Tipos de Almacenes'
	_rec_name = 'descripcion'
	descripcion = fields.Char('Almacen',size=20,required=True,readonly=False, help='Descripcion del Tipo de Almacen')
	contrato = fields.Boolean('Tiene Contrato', required=False)
	cuenta = fields.Many2one('account.account','Cuenta',required = False, help='Cuenta contable del almacen')
	active = fields.Boolean('Activo', required = False,default=True)

	
