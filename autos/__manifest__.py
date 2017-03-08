# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
	'name':'Autos',
	'version':'1',
	"author": "Juan Carlos Limon / Moises Velez",
	"category":"Agencias",
	'description': """
			Modulo de Venta de Autos
			""",
	"website": "http://www.google.com.mx/",
	"license":"AGPL-3",
	"depends":["sale","account","account_accountant","purchase","fleet"],
	"init_xml":[],
	"demo":[],
	"data":[
					

					# Load Views
					"catalogs/views/accesorios.xml",
					"catalogs/views/tipo_vehiculo.xml",
					"catalogs/views/tipo_motor.xml",
					"catalogs/views/color_interior.xml",
					"catalogs/views/color_exterior.xml",
					"catalogs/views/isan.xml",
					"catalogs/views/tenencia.xml",
					"catalogs/views/tipo_gasto.xml",
					"catalogs/views/tipo_transmision.xml",
					"catalogs/views/concepto_rebate_f.xml",
					"catalogs/views/almacenes.xml",
					"catalogs/views/ubicaciones.xml",
					"catalogs/views/tipo_venta.xml",
					"catalogs/views/tipo_compra.xml",
					"catalogs/views/factor_tenencia.xml",
					"catalogs/views/marcas.xml",
					"catalogs/views/tipo_auto.xml",
					"catalogs/views/version.xml",
					"purchases/views/compras.xml",
					
					# Load Data Default
					"data_view/estatus_vin.xml",
					# "data_view/tipo_rebate.xml",
					"data_view/marcas.xml",
					"data_view/tipo_motor.xml",
					"data_view/tipo_vehiculo.xml",
					"data_view/tipo_transmision.xml",
					"data_view/ubicaciones.xml",
					"data_view/tipo_venta.xml",
					"data_view/tipo_auto.xml",
					"data_view/estatus_compra.xml",
					
					"views/menu.xml",
					"views/product.xml",
				 ],
	"installable":True,
	"active": False,
	"application" : True,
}
