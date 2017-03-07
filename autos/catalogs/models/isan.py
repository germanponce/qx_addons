# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_isan(models.Model):
	_name= 'autos.catalogo.isan'
	_description='Catalogo ISAN'
	limite_inferior = fields.Float("Limite Inferior", digts=(2,5), help='Limite Inferior')
	limite_superior = fields.Float("Limite Superior", digits=(2,5), help='Limite Superior')
	porcentaje = fields.Float("Procentaje", digits=(2,5), help='Porcentaje')
	cuota = fields.Float("Cuota", digits=(2,5), help='Cuota')
	cargo = fields.Boolean('Cargo')

