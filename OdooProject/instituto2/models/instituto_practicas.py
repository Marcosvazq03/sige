# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
# from datetime import date, timedelta, datetime
# from odoo.exceptions import UserError

class InstitutoPracticas(models.Model):
    _name = "instituto2.practicas"
    _description = "Tabla de las practicas"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_practicas

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(string='Practicas')
    anio = fields.Char(required=True, string='Año de realización de las prácticas', size = 4, default = "2023")
    aprobado = fields.Boolean(string='Aprobado')

    # Campos que relacionan los alumnos y las empresas

    empresa_id = fields.Many2one("instituto2.empresa", string="Empresa", required=True)
    alumno_id = fields.Many2one("instituto2.alumno", string="Alumno", required=True)

    