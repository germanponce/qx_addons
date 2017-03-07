# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_motor(models.Model):
	_name= 'autos.catalogo.tipo.motor'
	_description='Tipo Motor'
	_rec_name='tipo_motor'

	tipo_motor = fields.Char('Tipo Motor',size=50,required=True,readonly=False, help='Tipo de Motor')
	active = fields.Boolean('Activo', default=True)

