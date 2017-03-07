# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_gasto(models.Model):
	_name= 'autos.catalogo.tipo.gasto'
	_description='Tipo de Gasto'
	_rec_name = 'descripcion'

	idTipoGasto = fields.Char('Id Tipo Gasto',size=5,reqired=True,readonly=False, help='Identificador Tipo de Gasto')
	descripcion = fields.Char('Descripcion',size=100,reqired=True,readonly=False, help='Descripcion Tipo de Gasto')
