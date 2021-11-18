# -*- coding: utf-8 -*-
{
    'name': "superheroes",

    'summary': """About Superheroes and Supervillains""",

    'description': """A simple tool to link Superheroes with their Nemesis""",

    'author': "Victor D.",
    'website': "https://dc.fandom.com/wiki/DC_Comics_Database",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ['views.xml', ],
}
