# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class versiones_autos(models.Model):
    _name = 'versiones.autos'
    _description = 'Catalogo para Gestion de Versiones A.'
    _rec_name = 'brand_id'

    @api.model
    def _get_brand_default(self):
        print "######## EJECUTANDO _get_brand_default"
        conf_obj = self.env['agencias.configuracion']
        conf_id = conf_obj.search([])
        print "######## conf_id >>>> ",conf_id
        # Search = Listado de Registros que concuerden con la busqueda
        if conf_id:
            return conf_id[0].brand_default_id.id

    ### name
    ###### Atributos Estandar para todos los campos ########
    # required  = Campo Obligatorio
    # readonly  = Campo Solo Lectura
    # help      = Ayuda para el llenado de cada Campo
    brand_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.', default=_get_brand_default) ##Char, size

class agencias_configuracion(models.Model):
    _name = 'agencias.configuracion'
    _description = 'configuracion para el Modulo de Agencias'
    _rec_name = 'brand_default_id'

    brand_default_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.')
    
