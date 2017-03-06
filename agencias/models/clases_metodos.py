# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

type_vehicle = [('camioneta','Camioneta'),
                ('auto','Auto'),
                ('moto','Moto')]
fuel_type = [('gasoline', 'Gasolina'), ('diesel', 'Diesel'), ('electric', 'Electrico'), ('hybrid', 'Hibrido')]

class versiones_autos(models.Model):
    _name = 'versiones.autos'
    _description = 'Catalogo para Gestion de Versiones A.'
    # _rec_name = 'brand_id'

    @api.model
    def _get_brand_default(self):
        print "######## EJECUTANDO _get_brand_default"
        conf_obj = self.env['agencias.configuracion']
        conf_id = conf_obj.search([]) # Metodo Search Recibe un listado de condiciones, cada condicion consta de 3 partes, el campo a buscar, la condicionante y el valor.
        # if conf_id:
        #     return conf_id[0].brand_default_id.id
        print "######## conf_id >>>> ",conf_id.brand_default_id.image_medium
        self.env.cr.execute("""
            select brand_default_id from agencias_configuracion;
            """)
        cr_res = self.env.cr.fetchall()
        print "########## CONSULTA A BASE DE DATOS >>> ",cr_res
        # Search = Listado de Registros que concuerden con la busqueda
        if cr_res:
            return cr_res[0][0]

    ### name
    ###### Atributos Estandar para todos los campos ########
    # required  = Campo Obligatorio
    # readonly  = Campo Solo Lectura
    # help      = Ayuda para el llenado de cada Campo
    brand_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.', default=_get_brand_default) ##Char, size
    type_car_id = fields.Many2one('agencias.tipo.auto','Tipo de Auto') ##Char, size
    name = fields.Char('Version', size=128, required=True)
    type_vehicle_id = fields.Selection(type_vehicle,'Tipo de Vehiculo', default="camioneta") ##Char, size
    key_v = fields.Char('Clave Comercial', size=128)
    key_c = fields.Char('Clave Vehicular', size=128)
    fuel_type = fields.Selection(fuel_type,'Tipo Motor') ##Char, size
    passengers = fields.Integers('Pasajeros')
    cylinders = fields.Integers('Cilindros')

class agencias_tipo_auto(models.Model):
    _name = 'agencias.tipo.auto'
    _description = 'Tipo de Auto'

    char = fields.Char('Tipo de Auto', required=True)

class agencias_configuracion(models.Model):
    _name = 'agencias.configuracion'
    _description = 'configuracion para el Modulo de Agencias'
    _rec_name = 'brand_default_id'

    brand_default_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.')
    
#### Una Marca puede tener N cantidad de Tipos de Auto