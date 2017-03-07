# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _

class autos_catalogo_factortenencia(models.Model):
	_name= 'autos.catalogo.factortenencia'
	_description='Catalogo de los factores de tenencia'
	rec_name = 'factor'
	mes=fields.Integer('Mes',size=2,required=True,readonly=False, help='Mes al que aplica el factor Enero=1,Febrero=2')
	factor=fields.Float('Factor del Mes',digits=(1,5),required=True,readonly=False, help='Factor de porcentaje que le corresponde segun al mes de venta')
	active=fields.Boolean('Activo',default=True)

	

