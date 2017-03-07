# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_marcas(models.Model):
	_name= 'autos.catalogo.marcas'
	_description='Catalogo de las marcas de los Autos'
	_rec_name = 'marca'

	marca=fields.Char('Marca',size=50,required=True,readonly=False, help='Descripcion de la marca del auto')
	cuenta=fields.Many2one('account.account','Cuenta Contable',required = False, help='Cuenta contable de la Marca')
	espropia=fields.Boolean('Es la Marca Propia', help='Es para saber si esta marca es la propia de la agencia')
	active=fields.Boolean('Activo',default=True)

