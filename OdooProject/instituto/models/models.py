from odoo import models, fields, api

# Definimos la clase TutoriaFCT que representa una tutoría de FCT en el instituto.
class TutoriaFCT(models.Model):
    _name = 'instituto.tutoriafct'  # Nombre del modelo

    # Campos del modelo
    nombre_tutor = fields.Char(string='Nombre del Tutor', required=True)  # Nombre del tutor
    email_tutor = fields.Char(string='Email del Tutor')  # Email del tutor
    telefono_tutor = fields.Char(string='Teléfono del Tutor')  # Teléfono del tutor
    alumnado_ids = fields.One2many('instituto.alumnado', 'tutoriafct_id', string='Alumnado')  # Relación con el modelo Alumnado

    @api.model
    def create(self, vals):
        vals['name'] = 'Nombre predeterminado'
        record = super(TutoriaFCT, self).create(vals)
        return record

# Definimos la clase Alumnado que representa a un alumno en el instituto.
class Alumnado(models.Model):
    _name = 'instituto.alumnado'  # Nombre del modelo

    # Campos del modelo
    nombre = fields.Char(string='Nombre', required=True)  # Nombre del alumno
    apellidos = fields.Char(string='Apellidos', required=True)  # Apellidos del alumno
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)  # Fecha de nacimiento del alumno
    direccion = fields.Char(string='Dirección')  # Dirección del alumno
    codigo_postal = fields.Char(string='Código Postal')  # Código postal del alumno
    email = fields.Char(string='Email')  # Email del alumno
    ciclo_formativo = fields.Selection([
        ('dam', 'DAM'),
        ('daw', 'DAW'),
        ('asir', 'ASIR'),
    ], string='Ciclo Formativo', default='dam', required=True)  # Ciclo formativo del alumno
    coche = fields.Boolean(string='Coche')  # Indica si el alumno tiene coche
    otros = fields.Text(string='Otros')  # Otros detalles del alumno
    nota_media = fields.Float(string='Nota Media', default=5.0)  # Nota media del alumno
    nota_media_texto = fields.Char(string='Nota Media en Texto', default='aprobado',
                                   compute='_compute_nota_media_texto')  # Nota media del alumno en texto
    empresa_id = fields.Many2one('instituto.empresa', string='Empresa')  # Relación con el modelo Empresa
    tutoriafct_id = fields.Many2one('instituto.tutoriafct', string='TutoriaFCT')  # Relación con el modelo TutoriaFCT

    # Método para calcular la nota media en texto
    def _compute_nota_media_texto(self):
        for record in self:
            if 0 <= record.nota_media < 5:
                record.nota_media_texto = 'suspendido'
            elif 5 <= record.nota_media < 7:
                record.nota_media_texto = 'aprobado'
            elif 7 <= record.nota_media < 9:
                record.nota_media_texto = 'notable'
            elif 9 <= record.nota_media <= 10:
                record.nota_media_texto = 'sobresaliente'

# Definimos la clase Empresa que representa a una empresa en el instituto.
class Empresa(models.Model):
    _name = 'instituto.empresa'  # Nombre del modelo

    # Campos del modelo
    nombre = fields.Char(string='Nombre', required=True)  # Nombre de la empresa
    direccion = fields.Char(string='Dirección')  # Dirección de la empresa
    telefono = fields.Char(string='Teléfono')  # Teléfono de la empresa
    departamento = fields.Selection([
        ('informatica', 'Informática'),
        ('comercio', 'Comercio'),
        ('marketing', 'Marketing'),
        ('administracion', 'Administración'),
    ], string='Departamento', default='informatica')  # Departamento de la empresa
    alumnado_ids = fields.One2many('instituto.alumnado', 'empresa_id', string='Alumnado')  # Relación con el modelo Alumnado
