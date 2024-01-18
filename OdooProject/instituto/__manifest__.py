{
    'name': 'Instituto',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Gestión de alumnado, empresas y tutorías FCT',
    'sequence': 10,
    'license': 'AGPL-3',
    'author': 'Marcos Vazquez',
    'depends': ['base'],
    'data': [
        'views/menu_principal.xml',
        'views/tutoriafct_view.xml',
        'views/alumnado_view.xml',
        'views/empresa_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}