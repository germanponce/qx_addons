# -*- encoding= utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from datetime import time, datetime
from odoo.tools.translate import _

class autos_catalogo_departamento(models.Model):
    _name = 'autos.catalogo.departamento'
    _description = 'Departamento'
    _rec_name = 'departamento'
    departamento = fields.Char(string='Departamento', size=40, required=True, readonly=False, help='Departamento')
    active = fields.Boolean(string='Activo', required=True, default=True)

