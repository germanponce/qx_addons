# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_auto(models.Model):
	_name= 'autos.catalogo.tipo.auto'
	_description='Tipos de Autos'
	_rec_name = 'descripcion'

	marca=fields.Many2one('autos.catalogo.marcas','Marca',required = True, help='Marca a la que pertenece el tipo de Auto')
	descripcion=fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion del Tipo de Auto')
	cuenta=fields.Many2one('account.account','Cuenta Contable',required = False, help='Cuenta contable del Tipo del Auto')
	active=fields.Boolean('Activo',default=True)

