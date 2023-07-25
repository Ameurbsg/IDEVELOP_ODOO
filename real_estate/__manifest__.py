# -*- coding: utf-8 -*-
{
    'name': "Real_estate",

    'summary': """
        Gestion des sociétés de Real Estate""",

    'description': """
        Gestion des appartements, loyers et ventes.
    """,

    'author': "Real Estate",
    'website': "https://www.energy-real-estate.ma/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',
    'application':True,
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'views/estate_property_views.xml',
    #     'views/templates.xml',
     ], 
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
