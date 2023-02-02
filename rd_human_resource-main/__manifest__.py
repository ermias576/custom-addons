{
    'name': 'R&D Employee',
    'author': 'R&D Developers',
    'category': 'Human Resources/Employees',
    'version': '1.0.0',
    'description': """Odoo 14 Employee Information""",
    'summary': 'Customization on the Employer and Employee Information',
    'sequence': 11,
    'website': 'https://randdethiopia.com/',
    'depends': ['crm','base_address_city','base','hr'],
    'license': 'LGPL-3',
    'data': [
       'views/Employee_address.xml'
    ],
     'application': True,
}
