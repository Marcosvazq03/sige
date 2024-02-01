{
    'name': 'Instituto',  # Nombre de la aplicación
    'version': '1.0',  # Versión de la aplicación
    'category': 'Education',  # Categoría de la aplicación
    'summary': 'Gestión de alumnado, empresas y tutorías FCT',  # Resumen de la aplicación
    'sequence': 10,  # Orden de la aplicación en el menú
    'license': 'AGPL-3',  # Licencia bajo la que se distribuye la aplicación
    'author': 'Marcos Vazquez',  # Autor de la aplicación
    'depends': ['base'],  # Módulos de los que depende la aplicación
    'data': [  # Archivos de datos que se cargarán con la aplicación
        'security/groups.xml',
        'security/tutoriafct.xml',
        'security/alumnado.xml',
        'security/empresa.xml',
        'views/menu_principal.xml',
        'views/tutoriafct/tutoriafct_view.xml',
        'views/tutoriafct/menu.xml',
        'views/alumnado/alumnado_view.xml',
        'views/alumnado/menu.xml',
        'views/empresa/empresa_view.xml',
        'views/empresa/menu.xml',
    ],
    'installable': True,  # Si la aplicación puede ser instalada
    'application': True,  # Si el módulo es una aplicación
    'auto_install': False,  # Si la aplicación se instala automáticamente
}