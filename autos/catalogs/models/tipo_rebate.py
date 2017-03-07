# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_tipo_rebate(models.Model):
	_name= 'autos.catalogo.tipo.rebate'
	_description='Tipo de Rebate'
	_rec_name = 'tipo_rebate'

	id_tipo_rebate = fields.Char('Id Tipo Rebate',size=5,reqired=True,readonly=False, help='Id Tipo Rebate')
	tipo_rebate = fields.Char('Descripcion',size=50,reqired=True,readonly=False, help='Tipo Rebate')
