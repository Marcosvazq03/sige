# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api

class InstitutoValoracion(models.Model):
    _name = "instituto2.valoracion"
    _description = "Tabla de las valoraciones de las empresas"

    # Para ver las tablas:
    # sudo su postgres
    # psql
    # \c dm2
    # \d instituto_valoracion

    # Tiene que tener si o si un atributo name porque sino coge el id
    name = fields.Char(required=True, string='Característica')
    nombre_color = fields.Selection(
        string='Color',
        selection=[('azul','Azul'), ('verde','Verde'), ('amarillo','Amarillo'), ('rojo','Rojo')], default = "azul",
        help="Color", required=True)

    # Para poder poner color hay que declarar un atributo Integer
    color = fields.Integer(compute="_color")

    # Dependiendo del color que elija en el desplegable se aplicará dicho código al campo Integer color
    @api.depends("nombre_color")
    def _color(self):
        for record in self:
            if record.nombre_color == "azul":
                record.color = 4
            else:
                if record.nombre_color == "verde":
                    record.color = 10
                else:
                    if record.nombre_color == "amarillo":
                        record.color = 3
                    else:
                        record.color = 1