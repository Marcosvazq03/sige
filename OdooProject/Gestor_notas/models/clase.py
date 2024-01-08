from odoo import models, fields

class Clase(models.Model):
    _name           = 'gestor.clase'
    _description    = 'Modelo para representar las clases ofrecidas por la institución'
    
    profesor_id     = fields.Many2one('gestor.profesor', string='Profesor encargado', required=True)
    name            = fields.Char(string='Nombre de la Clase', required=True)
    codigo_curso    = fields.Char(string='Código del Curso', required=True)
    materia         = fields.Char(string='Materia', required=True)