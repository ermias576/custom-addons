# -*- coding: utf-8 -*-
{
    'name': 'R&D Hospital',
    'version': '14.0.0.0.1',
    'summary': 'Hospital Managment System for odoo 14',
    'sequence': -100,
    'description': """R&D Group Hospital Managment System""",
    'category': 'Services',
    'author': 'Ermias Tegegn',
    'maintainer': 'Ermias Tegegn',
    'website': 'https://www.randdethiopia.com',
    'license': 'AGPL-3',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
