from odoo import api, fields, models

class InheritedEmployee(models.Model):
    _inherit = 'hr.employee'

    pension_id = fields.Char()
    tax_id = fields.Char()
    relationship = fields.Selection([
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('spouse', 'Spouse'),
        ('brother', 'Brother'),
        ('sister', 'Sister'),
        ('friend', 'Friend'),
        ('relative', 'Relative')
    ])
    city = fields.Many2one('res.city')
    sub_city = fields.Selection(
        [('addis_ketema', 'Addis Ketema'),
         ('akaky', 'Akaky Kaliti'),
         ('arada', 'Arada'),
         ('bole', 'Bole'),
         ('gullele', 'Gullele'),
         ('kirkos', 'Kirkos'),
         ('lideta', 'Lideta'),
         ('kolfe', 'Kolfe Keranio'),
         ('yeka', 'Yeka'),
         ('nifas_silk', 'Nifas Silk-Lafto'),
         ('lemi_kura', 'Lemi Kura')],
        default='bole')
    woreda = fields.Char()

    kebele = fields.Char()
    house_no = fields.Char()
    phone_number = fields.Char()
    bank_name = fields.Selection([
        ('abyssinia', 'Bank of Abyssinia'),
        ('cbe', 'Commercial Bank of Ethiopia'),
        ('nib', 'Nib International Bank'),
        ('abay', 'Abay Bank'),
        ('addis', 'Addis International Bank'),
        ('awash', 'Awash International Bank'),
        ('Berhan', 'Berhan International Bank'),
        ('bunna', 'Bunna International Bank'),
        ('oromia', 'Cooperative Bank of Oromia'),
        ('dashen', 'Dashen Bank'),
        ('debub', 'Debub Global Bank'),
        ('enat', 'Enat Bank')],
        default='abyssinia')
    bank_account_number = fields.Char()

class SubcityCityName(models.Model):
    _inherit = 'res.partner'
    
    sub_city_name1 = fields.Selection(
        [('addis_ketema', 'Addis Ketema'),
         ('akaky', 'Akaky Kaliti'),
         ('arada', 'Arada'),
         ('bole', 'Bole'),
         ('gullel', 'Gullele'),
         ('kirkos', 'Kirkos'),
         ('lideta', 'Lideta'),
         ('kolfe', 'Kolfe Keranio'),
         ('yeka', 'Yeka'),
         ('nifas_silk', 'Nifas Silk-Lafto'),
         ('lemi_kura', 'Lemi Kura')],
        default='bole')
    woreda1 = fields.Char()
    kebele1 = fields.Char()
    


