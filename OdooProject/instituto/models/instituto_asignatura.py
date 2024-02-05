# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class InstitutoAsignatura(models.Model):
    _name = "instituto.asignatura"
    _description = "Tabla de los diferentes asignaturas"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_asignatura

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Nombre')
