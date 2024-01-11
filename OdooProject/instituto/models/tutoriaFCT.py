from odoo import models, fields

class TutoriaFCT(models.Model):
    _name = 'instituto.tutoriafct'

    nombre_tutor = fields.Char(string='Nombre del Tutor', required=True)
    email_tutor = fields.Char(string='Email del Tutor')
    telefono_tutor = fields.Char(string='Teléfono del Tutor')
    alumnado_ids = fields.One2many('instituto.alumnado', 'tutoriafct_id', string='Alumnado')
