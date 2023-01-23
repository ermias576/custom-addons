# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'R&D Recuritment',
    'author': 'Odoo Mates',
    'category': 'Accounting',
    'version': '1.0.0',
    'description': """Odoo 14 Recurring Payment, Recurring Payment In Odoo, Odoo 14 Accounting""",
    'summary': 'Use recurring payments to handle periodically repeated payments',
    'sequence': 11,
    'website': 'https://www.odoomates.tech',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
       'views/inherited_recuritment_view.xml',
    ],
     'application': True,
}