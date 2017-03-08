# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api,exceptions
import odoo.addons.decimal_precision as dp


class autos_compras_datos_vin(models.Model):
    _name = 'autos.compras.datos.vin'
    vin = fields.Char('Vin', size=17, required=True)
    marca = fields.Many2one('autos.catalogo.marcas', 'Marca', required=True)
    aniomodelo = fields.Integer('Año Modelo', size=4, required=True)
    tipoauto = fields.Many2one('autos.catalogo.tipo.auto', 'Tipo Auto', required=True)
    version = fields.Many2one('autos.catalogo.version', 'Version', required=True)
    cvevehicular = fields.Char('Cve Vehicular', size=10, required=True)
    cvecomercial = fields.Char('Cve Comercial', size=10, required=True)
    fechamatriculacion = fields.Date('Fecha Matriculacion', required=True, help='Fecha de Matriculacion')
    placas = fields.Char('Placas', size=10, required=True)
    nummotor = fields.Char('No Motor', size=12, required=True)
    tipomotor = fields.Many2one('autos.catalogo.tipo.motor', 'Tipo Motor', required=True)
    tipotransmision = fields.Many2one('autos.catalogo.tipo.transmision', 'Tipo Transmision', required=True)
    nocilindros = fields.Integer('No Cilindros', size=2, required=True)
    nopuertas = fields.Integer('No Puertas', size=2, required=True)
    pasajeros = fields.Integer('Pasajeros', size=4, required=True)
    kilometraje = fields.Integer('Kilometraje', size=4, required=True)
    diasPiso = fields.Integer('Dias de Piso', size=4, required=True)


class autos_compras_documentos_extranjero(models.Model):
    _name = 'autos.compras.documentos.extranjero'
    contrato_Afasa = fields.Char('Contrato AFASA', size=20, required=True)
    pedimiento = fields.Char('Pedimiento', size=20, required=True)
    fechapedimiento = fields.Date('Fecha Pedimiento', required=True, help='Fecha de Pedimiento')
    aduana = fields.Char('Aduana', size=20, required=True)
    cuenta_contable_ext = fields.Many2one('account.account', 'Cuenta', required=False, help='Cuenta contable')


class autos_compras_precios(models.Model):
    _name = 'autos.compras.precios'

    def _default_iva(self):
       d_iva = self.env['account.tax'].search([('id', '=', 2)], limit=1).id
       return d_iva

    ajuste = fields.Float('Ajuste', digits=(10,5), readonly=False, help='Ajuste')
    precio_base = fields.Float('Precio Base', digits=(10,5), readonly=False, help='Precio Base')
    costo_total = fields.Float('Costo Total', digits=(10,5), readonly=True, help='Costo Total')
    cargos_adicionales = fields.Float('Cargos Adicionales', digits=(10,5), readonly=True, help='Cargos Adicionales')
    subtotal_base = fields.Float('Subtotal Base', digits=(10,5), readonly=True, help='Subtotal Base')
    holdback = fields.Float('Hold-Back', digits=(10,5), readonly=True, help='Hold-Back')
    holdbackcosto = fields.Float('HoldBack', digits=(10,5), readonly=True, help='Hold-Back')
    subtotal_compra = fields.Float('Subtotal Compra', digits=(10,5), readonly=True)
    iva_costo = fields.Many2one('account.tax', 'IVA', digits=(10,5), required=True, readonly=True, help='Iva del Costo', default=_default_iva)
    costo_iva = fields.Float('Monto Iva', digits=(10,5), readonly=True)
    total = fields.Float('Total', required=True, digits=(10,5), readonly=False, help='Total')

class autos_compras_datos_compra(models.Model):
    _name = 'autos.compras.datos.compra'

    def _default_iva(self):
        d_iva = self.env['account.tax'].search([('id', '=', 2)], limit=1).id
        return d_iva
		
    fechamatriculacion = fields.Date('Fecha Matriculacion', required=True, help='Fecha de Matriculacion')
    almacen = fields.Many2one('autos.catalogo.almacenes', 'Almacen', required=True)
    numero_inventario = fields.Char('Numero Inventario', size=20, required=True)
    departamentos = fields.Many2one('autos.catalogo.departamento', 'Departamentos', required=True)
    proveedor = fields.Many2one('res.partner', 'Proveedor', required=True, help='Proveedor al que se le hace la compra')
    tipocompra = fields.Many2one('autos.catalogo.tipo.compra', 'Tipo Compra', required=True)
    concesionario = fields.Boolean('Es Concesionario')
    estatus_compra = fields.Many2one('autos.catalogo.estatus.compra', 'Estatus de la Compra', required=True)
    esuntraspaso = fields.Boolean('Es traspaso')
    facturaproveedor = fields.Char('Factura', size=10, required=True)
    vencimiento = fields.Date('Fecha Vencimiento', required=True, help='Fecha en la que se vence el documento')
    iva = fields.Many2one('account.tax', 'IVA', required=True, help='Iva', default=_default_iva )
    estatus_vin = fields.Many2one('autos.catalogo.estatus.vin', 'Estatus Vin', required=True)


class autos_compras_equipo(models.Model):
    _name = 'autos.compras.datos.equipo'
    color_exterior = fields.Many2one('autos.catalogo.color.exterior', 'Color Exterior', required=True)
    precio_publico_ext = fields.Float('Precio Publico', digits=(5, 5), required=True, readonly=False, help='Precio Publico')
    distribuidor_ext = fields.Float('Distribuidor', digits=(5, 5), required=True, readonly=False, help='Distribuidor')
    color_interior = fields.Many2one('autos.catalogo.color.interior', 'Color Interior', required=True)
    precio_publico_int = fields.Float('Precio Publico', digits=(5, 5), required=True, readonly=False, help='Precio Publico')
    distribuidor_int = fields.Float('Distribuidor', digits=(5, 5), required=True, readonly=False, help='Distribuidor')


class autos_compras_datos_informacion(models.Model):
    _name = 'autos.compras.datos.informacion'
    codigo_motor = fields.Char('Codigo Motor', size=20, required=True)
    codigo_fabricacion = fields.Char('Codigo Fabricacion', size=20, required=True)
    numero_llave = fields.Char('Numero Llave', size=20, required=True)
    kilometraje_anual = fields.Char('Kilometraje Anual', size=20, required=True)
    todo_terreno = fields.Boolean('Todo Terreno')
    recurso = fields.Boolean('Es Recurso')
    documentacion = fields.Boolean('Contiene Documentacion')
    apartado = fields.Boolean('Apartado')
    vehiculo_transito = fields.Boolean('Vehiculo en Transito')


class autos_proceso_accesorio_compras(models.Model):
    _name = 'autos.proceso.accesorio.compras'
    _description = 'Relacion Accesorio/Compra/VIN'
    cod_accesorio = fields.Many2one('autos.catalogo.accesorios', 'Accesorios', required=True)
    serie = fields.Boolean('Serie')
    agregado = fields.Boolean('Agregado')


class autos_proceso_compras(models.Model):
    _name = 'autos.proceso.compras'
    _description = 'Compra de Autos nuevos a la planta y concesionarios'
    _inherits = {
        'autos.vin': 'autos_vin',
        'autos.compras.datos.vin': 'datosvin_id',
        'autos.compras.documentos.extranjero': 'extranjero_id',
        'autos.compras.precios': 'precios_id',
        'autos.compras.datos.compra': 'datoscompra_id',
        'autos.compras.datos.equipo': 'equipo_id',
        'autos.compras.datos.informacion': 'informacion_id',
    }

    def _default_estatus_compra(self):
        d_estatus_compra = self.env['autos.catalogo.estatus.compra'].search([('codestatus', '=', 'B')], limit=1).id
        return d_estatus_compra

    cod_compra = fields.Char('Cod Compra', help='Codigo Compra')
    nocompra = fields.Char('No Compra', help='No de compra que le asigna el sistema')
    fecha = fields.Date('Fecha Compra', required=True, default=fields.Date.today)
    autos_vin = fields.Many2one('autos.vin', required=True, ondelete='cascade')
    tipo_compra = fields.Many2one('autos.catalogo.tipo.compra', 'Tipo Compra', required=True)
    estatus_compra = fields.Many2one('autos.catalogo.estatus.compra', 'Estatus de la Compra', required=True, default=_default_estatus_compra, index=True)
    proveedor = fields.Many2one('res.partner', 'Proveedor', required=True, help='Proveedor al que se le hace la compra')
    facturaproveedor = fields.Char('Factura', size=10, required=True)
    vencimiento_factura = fields.Date('Fecha Vencimiento Factura', required=True,
                                      help='Fecha en la que se vence la Factura', default=fields.Date.today)
    propio = fields.Boolean('Es Propio')
    fecha_propio = fields.Date('Fecha Propio', required=False, default=fields.Date.today)
    traspaso = fields.Boolean('Es traspaso')
    accesorios = fields.Many2many('autos.catalogo.accesorios', 'autos_rel_catalogo_accesorio',
                                  'catalogo_ac_id', 'accesorio_a_id', string='Accesorios', required=False,
                                  help='Accesorios')

    @api.onchange('id_version')
    def onchange_version(self, id_version):
        res = {}
        if id_version:
            self._cr.execute(
                "SELECT accesorios_v_id FROM autos_rel_accesorio_versiones WHERE versiones_a_id = " + str(id_version))
            return {
                'domain': {
                    'accesorios': [('id', 'in', self._cr.fetchall())]
                }
            }

    @api.onchange('marca', 'tipoauto')
    def my_onchange_marca(self, marca, tipoauto, context=None):
        if context is None:
            context = {}
        res = {}
        if marca:
            res['tipoauto'] = False
            res['id_version'] = False
            res['accesorios'] = False
        if tipoauto:
            res['id_version'] = False
            res['accesorios'] = False
        return {'value': res}

    @api.onchange('ajuste','precio_base')
    def _calculacosto(self,ajustes,preciobase,context=None):
        d_iva = (self.env['account.tax'].search([('id', '=', 2)], limit=1).amount) /100
        if context is None:
            context={}
        res={}
        resultado = ajustes + preciobase
        res['costo_total']= resultado
        res['subtotal_compra'] = resultado
        res['costo_iva'] = d_iva * resultado
        res['total']= res['subtotal_compra'] + res['costo_iva']
        return {'value': res}

    @api.onchange('vin')
    def onchange_vin(self):
        result = self.VinValidate(self, self.vin)
        if not self.vin:
            return
        if result != 3:
            raise exceptions.except_orm(("Error!"), ("El numero de VIN es Invalido: " + str(self.vin.upper())))

    @staticmethod
    def VinValidate(self, value):

        if value == 0:
            return 0

        vin_data = value.upper()

        POSITIONAL_WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
        LETTER_KEY = dict(
            A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8,
            J=1, K=2, L=3, M=4, N=5, P=7, R=9,
            S=2, T=3, U=4, V=5, W=6, X=7, Y=8, Z=9,
        )
        numRomano = "X"
        largo = len(vin_data)

        digit_result = ""
        suma = 0
        i = 1
        if largo != 17:
            return 1
        else:
            for x in vin_data:
                if i != 9 and x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    suma += (int(x) * POSITIONAL_WEIGHTS[i - 1])
                elif i != 9 and x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    suma += (POSITIONAL_WEIGHTS[i - 1] * LETTER_KEY[x])
                i += 1

        resultado = (suma % 11)
        check_digit = vin_data[8]
        if resultado == 10:
            digit_result = "X"
        else:
            digit_result = resultado

        if str(resultado) != str(check_digit):
            return 2
        else:
            return 3

    @api.model
    def create(self, values):
        result=self.VinValidate(self,values['vin'])
        if result != 3:
            raise exceptions.except_orm(("Error!"),("El numero de VIN es Invalido: " + str(values['vin'])))
        else:
            return super(autos_proceso_compras, self).create(values)

    @api.multi
    def write(self, values):
        result = self.VinValidate(self,values['vin'])
        if result != 3:
            raise exceptions.except_orm(("Error!"),("El numero de VIN es Invalido: " + str(values['vin'])))
        else:
            return super(autos_proceso_compras, self).create(values)

    
class agencias_configuracion(models.Model):
    _name = 'agencias.configuracion'
    _description = 'configuracion para el Modulo de Agencias'
    _rec_name = 'brand_default_id'

    brand_default_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.')
    