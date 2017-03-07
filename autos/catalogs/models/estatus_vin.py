# -*- coding: utf-8 -*-

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_estatus_vin(models.Model):
	_name= 'autos.catalogo.estatus.vin'
	_description='Estatus para el vin Catalogo Interno'
	_rec_name = 'descripcion'
	
	idestatus   = fields.Char(string='id',size=1)
	descripcion = fields.Char(string='Descripcion',size=50)
	

	

