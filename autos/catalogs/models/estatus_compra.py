# -*- coding: utf-8 -*-

from odoo import fields, models
from datetime import time, datetime
from odoo.tools.translate import _


class autos_catalogo_estatus_compra(models.Model):
    _name = 'autos.catalogo.estatus.compra'
    _description = 'Estatus de la Compra'
    _rec_name = 'estatus'

    codestatus = fields.Char(string='Codigo', size=1)
    estatus = fields.Char(string='Estatus', size=50)




