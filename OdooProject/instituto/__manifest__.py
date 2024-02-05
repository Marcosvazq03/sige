# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Feb24Marcos',
    'version': '1.0',
    'category': 'Technical',
    'description': 'Módulo instituto',
    'author': 'DM2',
    'summary': 'Practicas de alumnos de FP',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/instituto_alumno_views.xml',
        'views/instituto_practicas_views.xml',
        'views/instituto_valoracion_views.xml',
        'views/instituto_empresa_views.xml',
        'views/instituto_profesor_views.xml',
        'views/instituto_asignatura_views.xml',
        'views/instituto_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False
}
