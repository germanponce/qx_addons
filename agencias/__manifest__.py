# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Modulo Curso Odoo',
    'version' : '1.1',
    'description': """

Este modulo permite practicar la programación de Odoo.

    """,
    'category': 'Educacion',
    'website': 'https://www.argil.mx',
    'depends' : ['fleet','mail'],
    'data': [
    'views/formularios_vistas.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': False,
}
