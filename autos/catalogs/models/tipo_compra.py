# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_compra(models.Model):
	_name= 'autos.catalogo.tipo.compra'
	_description='Catalogo Tipos de Compras'
	_rec_name='descripcion'

	descripcion=fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion del tipo de compra')
	active=fields.Boolean('Activo',default=True)
