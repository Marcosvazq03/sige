# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import date

from odoo import fields, models, api

class InstitutoAlumno(models.Model):
    _name = "instituto.alumno"
    _description = "Tabla de los diferentes alumnos"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_alumno

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Nombre')
    ap = fields.Char(required=True, string='Apellidos')
    fechNac = fields.Datetime(required=True, string='Fecha de nacimiento')
    dir = fields.Char(string='Dirección')
    codPostal = fields.Char(string='Código Postal')
    email = fields.Char(string='Email')
    ciclo = fields.Selection(
        string='Ciclo formativo',
        selection=[('dam', 'DAM'), ('daw', 'DAW'), ('asir', 'ASIR')], default="dam", required=True,
        help="Ciclo formativo")
    coche = fields.Boolean(string='Coche')
    otros = fields.Char(string='Otros')
    actitud = fields.Float(string='Actitud')
    ejercicios_clase = fields.Float(string='Ejercicios de Clase')
    proyecto = fields.Float(string='Proyecto')
    examen_proyecto = fields.Float(string='Examen sobre el Proyecto')
    nota_media = fields.Float(string='Nota Media', compute='_compute_nota_media')

    @api.constrains('fechNac')
    def check_edad(self):
        for record in self:
            if record.fechNac:
                fecha_nacimiento = fields.Date.from_string(record.fechNac)
                edad = date.today().year - fecha_nacimiento.year
                if ((date.today().month, date.today().day) < (fecha_nacimiento.month, fecha_nacimiento.day)):
                    edad -= 1
                if edad < 16:
                    raise models.ValidationError('El alumno debe tener al menos 16 años.')

    @api.depends('actitud', 'ejercicios_clase', 'proyecto', 'examen_proyecto')
    def _compute_nota_media(self):
        for record in self:
            record.nota_media = 0.05 * record.actitud + 0.20 * record.ejercicios_clase + 0.55 * record.proyecto + 0.20 * record.examen_proyecto

    # Campo empresa
    empresa_id = fields.Many2one("instituto.empresa", string="Empresa", required=True)


    

