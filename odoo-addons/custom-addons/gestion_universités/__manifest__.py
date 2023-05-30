# -*- coding: utf-8 -*-
{
    'name': "GestionUniversités",

    'summary': """
        Géstion d'une université""",

    'description': """
        Un module dans odoo pour gérer tous les entités dans une université
    """,

    'author': "Ifaliana",
    'website': "http://www.linanirina.com",

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
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
