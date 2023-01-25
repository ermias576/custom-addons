from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"


    name = fields.Char(string='Name', required=True, tracking=True)
    reference = fields.Char(string='Referenace', required=True, copy=False, readonly=True, 
                            default=lambda self: _('New'))
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other')
    ], required=True, default = 'male', tracking=True)

    note= fields.Text(String='Description', tracking=True)
    state= fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                             ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string="Status", tracking=True)

    responsible_id = fields.Many2one('res.partner', string="Responsible")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'    
        
    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create (self, vals):
        if not vals.get('not'):
            vals['note'] = 'New Patinet'
        return super(HospitalPatient, self).create(vals)    