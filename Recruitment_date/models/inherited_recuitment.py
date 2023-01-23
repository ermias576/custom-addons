from odoo import api, fields, models
from datetime import datetime



class InheritedRecuritment(models.Model):
    _inherit = 'hr.job'

    closed_date = fields.Date()