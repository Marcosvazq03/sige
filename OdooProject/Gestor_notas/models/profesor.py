from odoo import models, fields

class Profesor(models.Model):
    _name           = 'gestor.profesor'
    _description    = 'Modelo para representar a los profesores'

    name            = fields.Char(string='Nombre', required=True)
    apellido        = fields.Char(string='Apellido', required=True)
    no_identif      = fields.Char(string='Número de Identificación', required=True)