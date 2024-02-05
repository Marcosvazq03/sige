# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

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
        selection=[('dam','DAM'), ('daw','DAW'), ('asir','ASIR')], default = "dam", required=True,
        help="Ciclo formativo")
    coche = fields.Boolean(string='Coche')
    otros = fields.Char(string='Otros')
    media = fields.Float(string='Nota Media', default = "5.0")

    # Calcular el campo de texto de la media
    mediaTxt = fields.Char(string='Nota Media', default = "Aprobado", compute="_media_txt", readonly=True)
    
    @api.depends("media")
    def _media_txt(self):
        for record in self:
            if record.media < 5:
                record.mediaTxt = "Suspenso"
            else:
                if record.media < 7:
                    record.mediaTxt = "Aprobado"
                else:
                    if record.media < 9:
                        record.mediaTxt = "Notable"
                    else:
                        record.mediaTxt = "Sobresaliente"

    # Campo empresa
    empresa_id = fields.Many2one("instituto.empresa", string="Empresa", required=True)


    

