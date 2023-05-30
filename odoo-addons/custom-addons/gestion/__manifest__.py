# -*- coding: utf-8 -*-
{
    'name': "gestion",

    'summary': """
        Gestion université""",

    'description': """
        déscription du gestion de l'université
    """,

    'author': "Ifaliana",
    'website': "http://www.lina_nirina.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/professor_views.xml',
        'views/subject_views.xml',
        'views/classroom_views.xml',
        'views/department_views.xml',
        'views/teste_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
