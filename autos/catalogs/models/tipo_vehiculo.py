# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_vehiculo(models.Model):
	_name= 'autos.catalogo.tipo.vehiculo'
	_description='Tipo Vehiculo'
	_rec_name = 'tipo_vehiculo'

	tipo_vehiculo = fields.Char('Tipo Vehiculo',size=50,reqired=True,readonly=False, help='Tipo Vehiculo')
	active = fields.Boolean('Activo', reqired = True,default=True)


	
