# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_transmision(models.Model):
	_name= 'autos.catalogo.tipo.transmision'
	_description='Tipo de Transmision'
	_rec_name = 'descripcion'

	descripcion = fields.Char('Descripcion',size=100,reqired=True,readonly=False, help='Descripcion Tipo de Transmision')
