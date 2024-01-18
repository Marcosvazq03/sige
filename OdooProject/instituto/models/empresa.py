from odoo import models, fields

class Empresa(models.Model):
    _name = 'instituto.empresa'
    _description = 'Empresa'

    nombre = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    departamento = fields.Selection([
        ('informatica', 'Informática'),
        ('comercio', 'Comercio'),
        ('marketing', 'Marketing'),
        ('administracion', 'Administración'),
    ], string='Departamento', default='informatica')
    alumnado_ids = fields.One2many('instituto.alumnado', 'empresa_id', string='Alumnado')
