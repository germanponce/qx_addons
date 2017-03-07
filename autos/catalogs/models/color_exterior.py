#-*- encoding= utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_color_exterior(models.Model):
	_name= 'autos.catalogo.color.exterior'
	_description='Color Exterior'
	_rec_name = 'color'
	code_color = fields.Char(string='Codigo de Color Exterior',size=5,required=True,readonly=False, help='Codigo de Color Exterior')
	color = fields.Char(string='Color Exterior',size=50,required=True,readonly=False, help='Color Exterior')
	active = fields.Boolean(string='Activo', required = True,default=True)
	#versiones= fields.Many2many('autos.catalogo.version','autos_rel_color_ext_versiones','color_ext_v_id','versiones_ce_id',string = 'versiones',required = False, help='Versiones')

	
	
