{
    'name': 'Módulo de gestión de notas',
    'summary': 'Módulo para realizar la gestión de notas y alumnos.',
    'description': 'Este módulo puede ser utilizado por alumnos, maestros y padres para visualizar y gestionar las notas de los alumnos en sus actividades.',
    'version': '1.0.0',
    'category': 'Human Resources',
    'author': 'Christofer Borrayo',
    'data': [
        'security/groups.xml',
        'security/clase.xml',
        'security/estudiante.xml',
        'security/profesor.xml',
        'security/calificacion.xml',

        'views/menu_principal.xml',

        'views/clase/view_form.xml',
        'views/clase/view_tree.xml',
        'views/clase/menu.xml',

        'views/estudiante/view_form.xml',
        'views/estudiante/view_tree.xml',
        'views/estudiante/menu.xml',

        'views/profesor/view_form.xml',
        'views/profesor/view_tree.xml',
        'views/profesor/menu.xml',

        'views/calificacion/view_form.xml',
        'views/calificacion/view_tree.xml',
        'views/calificacion/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}