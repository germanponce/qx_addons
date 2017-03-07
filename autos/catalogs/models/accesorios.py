# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_accesorios(models.Model):
	_name= 'autos.catalogo.accesorios'
	_description='Catalogo Accesorios'
	_rec_name = 'descripcion'

	idAccesorio = fields.Char('Codigo del Acceso',size=5,required=True,readonly=False, help='Codigo del Accesorio')
	descripcion = fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion')
	descripcion_corta = fields.Char('Descripcion Corta',size=8,required=True,readonly=False, help='Descripcion Corta')
	active = fields.Boolean('Activo',invisible= True,default=True)
	#versiones = fields.Many2many('autos.catalogo.version','autos_rel_accesorio_versiones','accesorios_v_id','versiones_a_id',string = 'versiones',required = False, help='Versiones')	
	
	
	
