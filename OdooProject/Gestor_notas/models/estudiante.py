from odoo import models, fields

class Estudiante(models.Model):
    _name           = 'gestor.estudiante'
    _description    = 'Modelo para representar a los estudiantes'

    name            = fields.Char(string='Nombre', required=True)
    apellido        = fields.Char(string='Apellido', required=True)
    carnet          = fields.Char(string='Número de Identificación', required=True)