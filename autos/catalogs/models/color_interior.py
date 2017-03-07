#-*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_color_interior(models.Model):
	_name= 'autos.catalogo.color.interior'
	_description='Color Interior'
	_rec_name = 'color'
	code_color = fields.Char('Codigo de Color Interior',size=5,reqired=True,readonly=False, help='Codigo de Color Interior')
	color = fields.Char('Color Interior',size=50,reqired=True,readonly=False, help='Color Interior')
	active = fields.Boolean('Activo', required = True,default=True)
	#'versiones': fields.many2many('autos.catalogo.version','autos_rel_color_int_versiones','color_int_v_id','versiones_ci_id',string = 'versiones',required = False, help='Versiones'),		
	
	
	
