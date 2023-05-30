# -*- coding: utf-8 -*-
{
    'name': "universiter",

    'summary': """
        Géstion universiter""",

    'description': """
        Une module pour gérer tous les entités dans une université
    """,

    'author': "Ifaliana/Maricène",
    'website': "http://www.LinaNirina.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'University Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views_etudiant.xml',
        'views/views_enseignant.xml',
        'views/views_filiere.xml',
        'views/views_matiere.xml',
        'views/views_classe.xml',
        'views/views_ecolage.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
