# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class InstitutoEmpresa(models.Model):
    _name = "instituto.empresa"
    _description = "Tabla de las diferentes empresas"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_empresa

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Nombre')
    dir = fields.Char(string='Dirección')
    telf = fields.Char(string='Teléfono', size = 9)
    depar = fields.Selection(
        string='Departamento',
        selection=[('informática','Informática'), ('comercio','Comercio'), ('marketing','Marketing'), ('administración','Administración')], default = "informática",
        help="Departamento")

    # Si en el xml ponemos: <button name="accion_servidor" type="object" string="Ayuda"/>
    # Nos aparece un botón con un hipervínculo si descomentamos además la función:

    # def accion_servidor(self):
    #     return {
    #         "type": "ir.actions.act_url",
    #         "url": "https://odoo.com",
    #         "target": "self",
    #     }

    # Lista de alumnos que han hecho practicas en esa empresa
    # El string es el nombre de la cabecera cuando sale un popup para crear un nuevo alumno y el alumnos_id es el atributo que relaciona la tabla alumnos con las empresas en la tabla alumnos
    practicas_ids = fields.One2many("instituto.practicas", "empresa_id", string=' Alumnos')

    # Se relaciona con la tabla valoracion
    valoraciones_ids = fields.Many2many("instituto.valoracion", string="Valoraciones")
