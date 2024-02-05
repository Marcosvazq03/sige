from odoo import models, fields


class TutoriaFCT(models.Model):
    _name = 'instituto.tutoriafct'

    nombre_tutor = fields.Char(string='Nombre del Tutor', required=True)
    email_tutor = fields.Char(string='Email del Tutor')
    telefono_tutor = fields.Char(string='Teléfono del Tutor')
    alumnado_ids = fields.One2many('instituto.alumnado', 'tutoriafct_id', string='Alumnado')

class Alumnado(models.Model):
    _name = 'instituto.alumnado'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    direccion = fields.Char(string='Dirección')
    codigo_postal = fields.Char(string='Código Postal')
    email = fields.Char(string='Email')
    ciclo_formativo = fields.Selection([
        ('dam', 'DAM'),
        ('daw', 'DAW'),
        ('asir', 'ASIR'),
    ], string='Ciclo Formativo', default='dam', required=True)
    coche = fields.Boolean(string='Coche')
    otros = fields.Text(string='Otros')
    nota_media = fields.Float(string='Nota Media', default=5.0)
    empresa_id = fields.Many2one('instituto.empresa', string='Empresa')
    tutoriafct_id = fields.Many2one('instituto.tutoriafct', string='TutoriaFCT')




Dentro de la vista lista del objeto

class Empresa(models.Model):
    _name = 'instituto.empresa'

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
