# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import fields, models
from datetime import time, datetime
from odoo.tools.translate import _

class autos_vin(models.Model):
    _name = 'autos.vin'
    _description = 'VIN'
    _rec_name = 'vin'
    cod_vin = fields.Char('Code VIN', size=17, required=False, readonly=False, help='Code VIN')
    vin = fields.Char('VIN', size=17, required=False, readonly=False, help='VIN')
    anio_modelo = fields.Integer('Anio Modelo', size=4, required=False)
    fecha_matriculacion = fields.Date('Fecha Matriculacion', required=False)
    kilometraje = fields.Integer('Kilometraje', size=4, required=False)
    placas = fields.Char('Placas', size=8, required=False, readonly=False, help='Placas')
    descripcions = fields.Char('Descripcion', size=8, required=False, readonly=False, help='Descripcion')
    id_marca = fields.Many2one('autos.catalogo.marcas', 'Marca', required=False)
    id_tipo_auto = fields.Many2one('autos.catalogo.tipo.auto', 'Tipo Auto', required=False)
    id_version = fields.Many2one('autos.catalogo.version', 'Version', required=False)
    active = fields.Boolean('Activo', required=False, default=True)


