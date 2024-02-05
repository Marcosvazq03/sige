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


class Alumno(models.Model):
    _name = 'alumno'

    actitud = fields.Float(string='Actitud')
    ejercicios_clase = fields.Float(string='Ejercicios de Clase')
    proyecto = fields.Float(string='Proyecto')
    examen_proyecto = fields.Float(string='Examen sobre el Proyecto')
    nota_media = fields.Float(string='Nota Media', compute='_compute_nota_media')

    @api.depends('actitud', 'ejercicios_clase', 'proyecto', 'examen_proyecto')
    def _compute_nota_media(self):
        for record in self:
            record.nota_media = 0.05 * record.actitud + 0.20 * record.ejercicios_clase + 0.55 * record.proyecto + 0.20 * record.examen_proyecto





en una clase de odoo tengo un atributo notas con 4 campos: 5% actitud,20% ejercicios de clase, 55% proyecto, 20% examen sobre el propio proyecto. En el atributo nota_media tiene que generarse solo teniendo encuenta los % con las notas que introduzca el usuario
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
