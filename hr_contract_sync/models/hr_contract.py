from odoo import api, fields, models

class HrContract(models.Model):
    _inherit = 'hr.contract'

    def _create_resume_line(self, line_type):
       self.env['hr.resume.line'].create({
            'employee_id': self.employee_id.id,
            'name': self.job_id.name if self.job_id else '',
            'date_start': self.date_start,
            'date_end': self.date_end,
            'description': self.work_location_id.name if self.work_location_id else '',
            'contract_id': self._origin.id,
            'line_type_id': line_type and line_type.id,
        })

    def _update_resume_line(self):
        resume = self.env['hr.resume.line'].search([('contract_id', '=', self._origin.id)]) 
        resume.write({
            'name': self.job_id.name if self.job_id else '',
            'date_start': self.date_start,
            'date_end': self.date_end,
            'description': self.work_location_id.name if self.work_location_id else '',
        })

    @api.onchange('state')
    def onchange_state(self):
        self.ensure_one()
        if(self.state == 'open' or self.state == 'close'):
            line_type = self.env.ref('hr_skills.resume_type_experience', raise_if_not_found=False)
            if self.env['hr.resume.line'].search_count([('contract_id', '=', self._origin.id)]) == 0:
                self.env['hr.resume.line'].create({
                    'employee_id': self.employee_id.id,
                    'name': self.job_id.name if self.job_id else '',
                    'date_start': self.date_start,
                    'date_end': self.date_end,
                    'description': self.work_location_id.name if self.work_location_id else '',
                    'contract_id': self._origin.id,
                    'line_type_id': line_type and line_type.id,
                })
            else:
                # Update resume
                resume = self.env['hr.resume.line'].search([('contract_id', '=', self._origin.id)]) 
                resume.write({
                    'name': self.job_id.name if self.job_id else '',
                    'date_start': self.date_start,
                    'date_end': self.date_end,
                    'description': self.work_location_id.name if self.work_location_id else '',
                })
