# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api,exceptions, _
import odoo.addons.decimal_precision as dp
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class autos_compras_datos_vin(models.Model):
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _name = 'autos.compras.datos.vin'
    vin = fields.Char('Vin', size=17, required=True, track_visibility='onchange')
    marca = fields.Many2one('autos.catalogo.marcas', 'Marca', required=True)
    aniomodelo = fields.Integer('Año Modelo', size=4, required=True)
    tipoauto = fields.Many2one('autos.catalogo.tipo.auto', 'Tipo Auto', required=False)
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

    def _get_sequence_inventory(self):
        sequence_inventory =""
        config_obj = self.env['agencias.configuracion']
        config_id = config_obj.search([])
        if config_id:
            config_id = config_id[0]
            sequence_inventory = config_id.sequence_inventory.next_by_id()
        return sequence_inventory

    fechamatriculacion = fields.Date('Fecha Matriculacion', required=True, help='Fecha de Matriculacion')
    almacen = fields.Many2one('autos.catalogo.almacenes', 'Almacen', required=True)
    numero_inventario = fields.Char('Numero Inventario', size=64, required=True, default=_get_sequence_inventory)
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

    @api.one
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        config_obj = self.env['agencias.configuracion']
        config_id = config_obj.search([])
        if config_id:
            config_id = config_id[0]
            sequence_inventory = config_id.sequence_inventory.next_by_id()
            default.update({'numero_inventario': sequence_inventory})
        return super(autos_proceso_compras, self).copy(default)

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
    _inherit = ['mail.thread', 'ir.needaction_mixin']
    _rec_name = 'sequence_name' 
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

    def _get_sequence_purchase(self):
        sequence_purchase =""
        config_obj = self.env['agencias.configuracion']
        config_id = config_obj.search([])
        if config_id:
            config_id = config_id[0]
            sequence_purchase = config_id.sequence_purchase.next_by_id()
        return sequence_purchase

    @api.depends('purchase_id.order_line.move_ids.picking_id')
    def _compute_picking(self):
        for order in self:
            pickings = self.env['stock.picking']
            if order.purchase_id:
                for line in order.purchase_id.order_line:
                    moves = line.move_ids.filtered(lambda r: r.state != 'cancel')
                    pickings |= moves.mapped('picking_id')
                order.picking_ids = pickings
                order.picking_count = len(pickings)
            else:
                order.picking_count = 0
                order.picking_ids = False

    @api.depends('purchase_id')
    @api.one
    def _compute_name_purchase(self):
        if not self.purchase_id:
            self.purchase_id_name = ""
        else:
            self.purchase_id_name = self.purchase_id.name

    cod_compra = fields.Char('Cod Compra', help='Codigo Compra', copy=False, track_visibility='onchange')
    nocompra = fields.Char('No Compra', help='No de compra que le asigna el sistema')
    fecha = fields.Date('Fecha Compra', required=True, default=fields.Date.today, track_visibility='onchange')
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

    purchase_id = fields.Many2one('purchase.order', 'Pedido de Compra', copy=False)
    state = fields.Selection([
                              ('draft','Borrador'),
                              ('confirmed','Confirmado'),
                              ('done','Cerrado'),
                              ('cancel','Cancelado'),
                              ], 'Estado', default='draft')

    sequence_name = fields.Char('Secuencia', size=128, default=_get_sequence_purchase)

    picking_count = fields.Integer(compute='_compute_picking', string='Conteo de Albaranes', default=0, copy=False)

    picking_ids = fields.Many2many('stock.picking', compute='_compute_picking', string='Recepciones de Compra', copy=False)

    purchase_id_name = fields.Char(compute='_compute_name_purchase', string='Compra', size=128, default="", copy=False)

    _order = 'id desc' 

    @api.multi
    def action_view_picking_purchase(self):
        '''
        This function returns an action that display existing picking orders of given purchase order ids.
        When only one found, show the picking immediately.
        '''
        action = self.env.ref('stock.action_picking_tree')
        print "########### ACTION >>>> ",action
        print "########### ACTION >>>> ",action.read()
        print "########### ACTION >>>> ",action.read()[0]
        result = action.read()[0]

        #override the context to get rid of the default filtering on picking type
        result['context'] = {}
        if not self.purchase_id:
            return True

        pick_ids = sum([order.purchase_id.picking_ids.ids for order in self], [])
        #choose the view_mode accordingly
        if len(pick_ids) > 1:
            result['domain'] = "[('id','in',[" + ','.join(map(str, pick_ids)) + "])]"
        elif len(pick_ids) == 1:
            res = self.env.ref('stock.view_picking_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = pick_ids and pick_ids[0] or False
        return result


    @api.multi
    def action_view_purchase(self):
        '''
        This function returns an action that display existing picking orders of given purchase order ids.
        When only one found, show the picking immediately.
        '''
        result = {}
        if self.purchase_id:
            if self.purchase_id.state in ('purchase','done'):
                action = self.env.ref('purchase.purchase_form_action')
            else:
                action = self.env.ref('purchase.purchase_rfq')

            result = action.read()[0]

            #override the context to get rid of the default filtering on picking type
            result['context'] = {}

            purchase_id = [self.purchase_id.id]
            #choose the view_mode accordingly
            res = self.env.ref('purchase.purchase_order_form', False)
            result['views'] = [(res and res.id or False, 'form')]
            result['res_id'] = purchase_id and purchase_id[0] or False
        return result

    @api.multi
    def action_view_purchase_invoice(self):
        if self.purchase_id:
            result = self.purchase_id.action_view_invoice()
            return result
        return True

    ## Consulta por Codigo de la secuencia
    # sequence_name = self.env['ir.sequence'].next_by_code('sale.order')

    @api.multi
    def draft(self, ):
        self.state = 'draft'
        user = self.env['res.users'].browse(self._uid)
        self.message_post(
                         body=_("Registro Confirmado.<br/>Confirmado por:<em>%s</em>.") % (user.name,))
    @api.multi
    def confirmed(self, ):
        self.state = 'confirmed'

    @api.multi
    def done(self, ):
        self.state = 'done'

    @api.multi
    def cancel(self, ):
        self.state = 'cancel'

    # @api.onchange('id_version')
    # def onchange_version(self, id_version):
    #     res = {}
    #     if id_version:
    #         self._cr.execute(
    #             "SELECT accesorios_v_id FROM autos_rel_accesorio_versiones WHERE versiones_a_id = " + str(id_version))
    #         return {
    #             'domain': {
    #                 'accesorios': [('id', 'in', self._cr.fetchall())]
    #             }
    #         }


    @api.onchange('id_version')
    def my_onchange_version(self,):
        list_accesorios_ids = []
        if self.id_version:
            for accesorio in self.id_version.accesorios:
                list_accesorios_ids.append(accesorio.id)
            self.update({'accesorios': [(6, 0, list_accesorios_ids)]})


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
            res = super(autos_proceso_compras, self).create(values)
            user = self.env['res.users'].browse(self._uid)
            res.message_post(
                            body=_("Gracias por usar el sistema de Compra de Autos.<br/>Bienvenido:<em>%s</em>.") % (user.name,))
            return res

    @api.multi
    def write(self, values):
        if 'vin' in values:
            result = self.VinValidate(self,values['vin'])
            if result != 3:
                raise exceptions.except_orm(("Error!"),("El numero de VIN es Invalido: " + str(values['vin'])))
            else:
                return super(autos_proceso_compras, self).write(values)
        else:
            return super(autos_proceso_compras, self).write(values)

    @api.one
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        config_obj = self.env['agencias.configuracion']
        config_id = config_obj.search([])
        if config_id:
            config_id = config_id[0]
            sequence_purchase = config_id.sequence_purchase.next_by_id()
            sequence_inventory = config_id.sequence_inventory.next_by_id()
            default.update({'sequence_name': sequence_purchase,
                'numero_inventario': sequence_inventory})
        return super(autos_proceso_compras, self).copy(default)

class purchase_order(models.Model):
    _inherit = 'purchase.order'

    compra_nuevos_id = fields.Many2one('autos.proceso.compras','Compra Autos Nuevos', readonly=True)
    

class agencias_configuracion(models.Model):
    _name = 'agencias.configuracion'
    _description = 'configuracion para el Modulo de Agencias'
    _rec_name = 'brand_default_id'

    brand_default_id = fields.Many2one('fleet.vehicle.model.brand','Marca', required=True, help='Define el nombre de la Version.')
    product_template_new_car = fields.Many2one('product.template','Producto Autos Nuevos', help='Estos campos ayudan a generar compras para Cada uno de los Casos.', )
    product_template_used_car = fields.Many2one('product.template','Producto Autos Usados', help='Estos campos ayudan a generar compras para Cada uno de los Casos.', )
    stock_picking_type = fields.Many2one('stock.picking.type','Regla de Recepcion', help='Indicara las reglas y ubicaciones por \
                                                                                            donde ingresara la mercancia hasta llegar al Almacen Principal.', )
    sequence_purchase = fields.Many2one('ir.sequence', 'Secuencia Compras')
    sequence_inventory = fields.Many2one('ir.sequence', 'Secuencia Inventarios')

    
    @api.one
    @api.constrains('id','brand_default_id')
    def _check_config(self):
        print "##### check config rule >>>>"
        if self.id and self.brand_default_id:
            other_id = self.search([('id','!=',self.id)])
            print "######## OTHER IDS >>>> ",other_id
            if other_id:
                raise ValidationError(_('Solo debe existir un registro de Configuracion.'))


class asistente_compra_autos(models.TransientModel):
    _name = 'asistente.compra.autos'
    _description = 'Asistente para generar ordenes de Compra'


    def _get_fecha(self):
        context = self._context
        active_id = context['active_id']
        compra_br = self.env['autos.proceso.compras'].browse(active_id)
        print "####### context ",context
        return compra_br.fecha if compra_br.fecha else False

    def _get_picking_type(self):
        config_obj = self.env['agencias.configuracion']
        config_id = config_obj.search([])
        if config_id:
            stock_picking_type = config_id[0].stock_picking_type.id if config_id[0].stock_picking_type else False
            return stock_picking_type

    fechacompra = fields.Date('Fecha para Compra', default=_get_fecha)
    fecha_prevista = fields.Date('Fecha Recepcion', default=fields.Date.today())
    stock_picking_type = fields.Many2one('stock.picking.type','Regla de Recepcion', help='Indicara las reglas y ubicaciones por \
                                                                                           donde ingresara la mercancia hasta llegar al Almacen Principal.', default=_get_picking_type )
    product_tmpl = fields.Many2one('product.template','Plantilla Compra Auto')
    
    product_id = fields.Many2one('product.product','Variante')

    comfirm_order = fields.Boolean('Confirmar Compra', help='Si se activa este campo el pedido de compra sera confirmado y se creara una entrada a Almacen.', )

    serial_number = fields.Many2one('stock.production.lot','No. Serie')

    serial_number_uniq = fields.Char('No. Serie Unico', size=128)

    tracking = fields.Char('Seguimiento Serie/Lote')

    @api.onchange('product_tmpl')
    def my_onchange_product_tmpl(self,):
        if self.product_tmpl:
            self.update({'tracking': self.product_tmpl.tracking})

    @api.multi
    def create_purchase(self):
        print "############ create_purchase "
        ### CONTEXT
        context = self._context
        active_ids = context['active_ids']
        active_id = context['active_id']
        print "############ context >>>>>>>> ",context
        compra_obj = self.env['autos.proceso.compras']
        compra_br = compra_obj.browse(active_id)

        no_confirmed_ids = compra_obj.search([('state','!=','confirmed'),
                                              ('id','in',active_ids)])
        if no_confirmed_ids:
            raise ValidationError(_('Uno o varios de los registros seleccionados\
                se encuentran en un estado Invalido.\n(Solo se puede generar compras\
                en registros confirmados)'))

        if len(active_ids) != 1:
            raise ValidationError(_('Solo puedes ejecutar el asistente sobre 1 registro en especifico.'))
        purchase_obj = self.env['purchase.order']


        vals = {
            'partner_id': compra_br.proveedor.id,
            'compra_nuevos_id': compra_br.id,
            'date_order': self.fechacompra,
            'date_planned': self.fecha_prevista,
            'picking_type_id': self.stock_picking_type.id,
        }
        purchase_id = purchase_obj.create(vals)

        purchase_line_obj = self.env['purchase.order.line']

        description = ""
        codigo_producto = "["+self.product_id.default_code+ "] " if self.product_id.default_code else ""
        accesorios = [str(x.descripcion) for x in compra_br.accesorios]
        description = codigo_producto+ self.product_id.name+"\n"+"Accesorios: "+str(accesorios)
        
        linea_compra = {
            'product_id': self.product_id.id,
            'product_qty': 1.0,
            'price_unit': compra_br.total,
            'name': description,
            'product_uom': self.product_id.uom_po_id.id,
            'date_planned': self.fecha_prevista,
            'taxes_id': [(6, 0, [compra_br.iva_costo.id])],
            'order_id': purchase_id.id,
        }

        purchase_line_obj.create(linea_compra)
        print "########### PEDIDO ID >>>> ",purchase_id
        compra_br.write({'purchase_id': purchase_id.id})
        compra_br.done()

        if self.comfirm_order:
            purchase_id.button_confirm()
            if self.tracking != 'none':
                print "###### tracking >>> "
                if self.tracking == 'serial':
                    if self.serial_number_uniq:
                        serial_number_uniq = self.serial_number_uniq
                        for picking in compra_br.picking_ids:
                            if picking.state != 'done':
                                for pk in picking.pack_operation_product_ids:
                                    if pk.product_id.id == self.product_id.id:
                                        if pk.pack_lot_ids:
                                            pk.pack_lot_ids.unlink()

                                        lot_operation = [(0,0,{'lot_name':serial_number_uniq})]
                                        pk.write({'pack_lot_ids': lot_operation})
                else:
                    if self.serial_number:
                        serial_number = self.serial_number.id
                        for picking in compra_br.picking_ids:
                            if picking.state != 'done':
                                for pk in picking.pack_operation_product_ids:
                                    if pk.product_id.id == self.product_id.id:
                                        if pk.pack_lot_ids:
                                            pk.pack_lot_ids.unlink()

                                        lot_operation = [(0,0,{
                                            'lot_name':self.serial_number.name,
                                            'qty': 1.0,
                                            })]
                                        pk.write({'pack_lot_ids': lot_operation})

        return {
                'domain': "[('id','in', ["+','.join(map(str,[purchase_id.id]))+"])]",
                'name': _('Compra de Autos Nuevos'),
                'view_type': 'form',
                'view_mode': 'tree,form',
                'res_model': 'purchase.order',
                'view_id': False,
                'type': 'ir.actions.act_window'
                }

    @api.multi
    def create_serial_number(self):
        print "########## CREANDO EL NO. SERIE >>>>"
        context = self._context
        active_id = context['active_id']
        compra_obj = self.env['autos.proceso.compras']
        compra_br = compra_obj.browse(active_id)
        serial_obj = self.env['stock.production.lot']
        serial_name = ""
        serial_name =  compra_br.vin+"/"+compra_br.nummotor
        print "######## self.product_tmpl.id ",self.product_tmpl.id
        print "######## serial_name ",serial_name

        product_id = self.product_id.id
        
        if self.product_id.tracking == 'serial':

            self.write({
            'fechacompra': self.fechacompra,
            'fecha_prevista': self.fecha_prevista,
            'stock_picking_type': self.stock_picking_type.id ,
            'product_tmpl': self.product_tmpl.id,
            'product_id': self.product_id.id,
            'serial_number_uniq': serial_name,

                })
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'asistente.compra.autos',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
                'context': self._context,
                }

        elif self.product_id.tracking == 'lot':
            exist_lot_number = serial_obj.search([('product_id','=',self.product_id.id),
                                                  ('name','=',serial_name)])
            serial_id = False
            if exist_lot_number:
                serial_id = exist_lot_number[0].id
            else:
                vals = {
                    'product_id': self.product_id.id,
                    'name': serial_name,
                }
                serial_result = serial_obj.create(vals)
                serial_id = serial_result.id

            self.write({
                'fechacompra': self.fechacompra,
                'fecha_prevista': self.fecha_prevista,
                'stock_picking_type': self.stock_picking_type.id ,
                'product_tmpl': self.product_tmpl.id,
                'product_id': self.product_id.id,
                'serial_number': serial_id,

                })
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'asistente.compra.autos',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
                'context': self._context,
                }
        else:
            self.write({
                'fechacompra': self.fechacompra,
                'fecha_prevista': self.fecha_prevista,
                'stock_picking_type': self.stock_picking_type.id ,
                'product_tmpl': self.product_tmpl.id,
                'product_id': self.product_id.id,
                })
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'asistente.compra.autos',
                'view_mode': 'form',
                'view_type': 'form',
                'res_id': self.id,
                'views': [(False, 'form')],
                'target': 'new',
                'context': self._context,
                }