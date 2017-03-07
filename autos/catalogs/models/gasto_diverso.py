# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_gastosdiversos(models.Model):
	_name= 'autos.catalogo.gastosdiversos'
	_description='Catalogo de gastos diversos del pedido'
	_rec_name = 'descripcion'
	descripcion=fields.Char('Descripcion',size=50,required=True,readonly=False, help='Descripcion de la ubicacion')
	tipogasto=fields.Selection([('T','Tenencia'),('P','Pedido')],String='Tipo Gasto',required=True,help='Poder identificar el tipo de gasto en donde y como se calculara')
	preciopublico=fields.Float('Precio Publico',digits=(5,2), help='Importe que se le cobrara al cliente')
	preciodistribuidor=fields.Float('Precio concesionario',digits=(5,2), help='Importe que e cuesta al concesionario')
	esfiscal=fields.Boolean('Es nota fiscal', help='Habilite la opcion si requiere que se haga fiscal la nota de cargo')
	active=fields.Boolean('Activo',default=True)

