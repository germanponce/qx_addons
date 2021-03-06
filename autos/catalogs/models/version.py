# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields,models,api
from datetime import time,datetime
from odoo.tools.translate import _


class autos_catalogo_version(models.Model):
    _name= 'autos.catalogo.version'
    _description='Version'
    _rec_name = 'version_auto'

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

    marcas=fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.', default=_get_brand_default) ##Char, size
    tipo_auto=fields.Many2one('autos.catalogo.tipo.auto','Tipo Auto',required = False, help='Tipo Auto')
    version_auto=fields.Char('Version',size=50,required=True,readonly=False, help='version')
    tipo_vehiculo= fields.Many2one('autos.catalogo.tipo.vehiculo','Tipo Vehiculo',required = False, help='Tipo Vehiculo')
    cve_comercial=fields.Char('Cve. Comercial',size=50,required=True,readonly=False, help='Clave Comercial')
    cve_vehicular=fields.Char('Cve. Vehicular',size=50,required=True,readonly=False, help='Clave Vehicular')
    tipo_motor= fields.Many2one('autos.catalogo.tipo.motor','Tipo Motor',required = False, help='Tipo de Motor')
    tipo_transmision= fields.Many2one('autos.catalogo.tipo.transmision','Tipo Transmision',required = False, help='Tipo de Transmision')
    cilindros=fields.Integer('Cilindros',size=2,required=True,readonly=False, help='Cilindros')
    puertas=fields.Integer('Puertas',size=2,required=True,readonly=False, help='Puertas')
    pasajeros=fields.Integer('Pasajeros',size=2,required=True,readonly=False, help='Pasajeros')
    precio_publico_mn=fields.Float('Publico MN',digits=(5,5),required=True,readonly=False, help='Precio Publico')
    precio_publico_me=fields.Float('Publico ME',digits=(5,5),required=True,readonly=False, help='Precio Publico')
    holdback=fields.Float('HoldBack',digits=(1,5),required=True,readonly=False, help='HoldBack')
    importacion = fields.Boolean('Es de Importacion')
    carga = fields.Boolean('Es un Auto para Carga')
    accesorios= fields.Many2many('autos.catalogo.accesorios','autos_rel_accesorio_versiones','versiones_a_id','accesorios_v_id',string = 'Accesorios',required = False, help='Accesorios')
    color_exterior= fields.Many2many('autos.catalogo.color.exterior','autos_rel_color_ext_versiones','versiones_ce_id','color_ext_v_id',string = 'Color Exterior',required = False, help='Color Exterior')
    color_interior= fields.Many2many('autos.catalogo.color.interior','autos_rel_color_int_versiones','versiones_ci_id','color_int_v_id',string = 'Color Interior',required = False, help='Color Interior')

    @api.onchange('marcas')
    def my_onchange_function(self,marcas,context=None):
        if context is None:
            context = {}
        res = {}
        if marcas:
                res['tipo_auto'] = False
        return {'value': res}