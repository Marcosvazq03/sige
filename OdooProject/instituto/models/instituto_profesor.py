# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class InstitutoProfesor(models.Model):
    _name = "instituto.profesor"
    _description = "Tabla de los diferentes profesores"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_profesor

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Nombre')
    apellidos = fields.Char(required=True, string='Apellidos')
    email = fields.Char(string='Email')
    departamento = fields.Selection(
        string='Ciclo formativo',
        selection=[('informatica', 'Informatica'), ('comercio', 'Comercio'), ('marketing', 'Marketing'), ('administracion', 'Administracion')], default="informatica", required=True,
        help="Departamento")
