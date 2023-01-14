from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"


    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default = 'male')

    note= fields.Text(String='Description')
    state= fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status")
