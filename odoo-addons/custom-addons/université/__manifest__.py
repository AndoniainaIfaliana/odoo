# -*- coding: utf-8 -*-
{
    'name': "Université",

    'summary': """
        Géstion université
        """,

    'description': """
        Une module pour gérer tous les entités dans une université
    """,

    'author': "Ifaliana/Maricène",
    'website': "http://www.LinaNirina.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/etudiant_views.xml',
        # 'views/prof_views.xml',
        # 'views/filiere_views.xml',
        # 'views/matiere_views.xml',
        # 'views/classe_views.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
