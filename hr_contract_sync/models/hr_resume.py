from odoo import api, fields, models

class ResumeLine(models.Model):
    _inherit = 'hr.resume.line'

    contract_id = fields.Many2one('hr.contract')