# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError

type_vehicle = [('camioneta','Camioneta'),
                ('auto','Auto'),
                ('moto','Moto')]
fuel_type = [('gasoline', 'Gasolina'), ('diesel', 'Diesel'), ('electric', 'Electrico'), ('hybrid', 'Hibrido')]

class versiones_autos(models.Model):
    _name = 'versiones.autos'
    _inherit = ['mail.thread', 'ir.needaction_mixin']
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
    key_v = fields.Char('Clave Comercial', size=128, copy=False)
    key_c = fields.Char('Clave Vehicular', size=128, copy=False)
    fuel_type = fields.Selection(fuel_type,'Tipo Motor') ##Char, size
    passengers = fields.Integer('Pasajeros')
    cylinders = fields.Integer('Cilindros')
    price_base = fields.Float('Precio Base', digits=(14,6))
    price_pb_mn = fields.Float('Publico MN', digits=(14,6))
    holdback = fields.Float('HoldBack', digits=(14,6))
    imp_y = fields.Boolean('Es de Importacion')
    ch_y = fields.Boolean('Es un Auto para Carga')
    transm_type = fields.Selection([
                                    ('automatico','Automatico'),
                                    ('estandar','Estandar'),
                                    ],'Tipo de Transmision')
    doors_n = fields.Integer('No. Puertas')
    image = fields.Binary('Imagen')

    @api.model # Self, cr, uid, ids, context
    def create(self, vals):
        print "######## VALS >>> ",vals
        doors_n = vals['doors_n'] if 'doors_n' in vals else False
        name = vals['name'] if 'name' in vals else False
        name = name.strip(' ')
        print "######### context >>> ", self._context
        print "######### DOOR N >>>> ", doors_n
        other_id = self.search([('name','=',name)])
        if other_id:
            raise UserError(_('El Registro ya existe en la Base de Datos, prueba con uno diferente.'))
        res = super(versiones_autos, self).create(vals)
        if not doors_n: ### 0, False,[],()= Null
            raise UserError(_('El campo No. de Puertas es Incorrecto.\nIngresa uno de los Valores: [3, 5]'))
        elif doors_n not in (3,5):
            raise UserError(_('El campo No. de Puertas es Incorrecto.\nIngresa uno de los Valores: [3, 5]'))
        print "############### CREATE >>> ",res
        ##### Recordset
        return res

    @api.multi
    def write(self, vals):
        print "######## WRITE >>> "
        print "######## VALS >>> ",vals
        print "######## IDS ", self._ids
        doors_n = vals['doors_n'] if 'doors_n' in vals else False
        if doors_n:
            if doors_n not in (3,5):
                raise UserError(_('El campo No. de Puertas es Incorrecto.\nIngresa uno de los Valores: [3, 5]'))
        name = vals['name'] if 'name' in vals else False
        if name:
            name = name.strip(' ')
            other_id = self.search([('name','=',name)])
            if other_id:
                raise UserError(_('El Registro ya existe en la Base de Datos, prueba con uno diferente.'))
            res = super(versiones_autos, self).write(vals)
        ##### Recordset
        return res

    @api.one
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        print "############## COPY >>>> "
        print "############## DEFAULT >>>> ",default
        default.update({
                'doors_n': 5,
                'name': self.name+" (COPIA)",
            })

        return super(versiones_autos, self).copy(default)


### Clase ORM
# Creacion = create
# Actualizacion = write
# Eliminacion = unlink
# Duplicado = copy
# Lectura = read

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