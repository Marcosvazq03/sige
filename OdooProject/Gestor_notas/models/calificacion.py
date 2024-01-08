from odoo import models, fields

class Calificacion(models.Model):
    _name           = 'gestor.calificacion'
    _description    = 'Modelo para almacenar las notas de los alumnos'

    estudiante_id   = fields.Many2one('gestor.estudiante', string='Estudiante', required=True)
    clase_id        = fields.Many2one('gestor.clase', string='Clase', required=True)
    nota            = fields.Float(string='Nota', required=True)
    fecha_calif     = fields.Date(string='Fecha de Calificación', required=True)