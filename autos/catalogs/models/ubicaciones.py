# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _



class autos_catalogo_ubicaciones(models.Model):
	_name= 'autos.catalogo.ubicaciones'
	_description='Catalogo Ubicacion de los Autos'
	_rec_name = 'descripcion'

	descripcion=fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion de la ubicacion')
	active=fields.Boolean('Activo',required=True,default=True)

	_sql_constraints = [
    ('descripcion_unique', 'descripcion', ("La descripcion de la ubicacion debe de ser unica!!"))
]

