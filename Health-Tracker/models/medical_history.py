from odoo import models, fields


class MedicalHistory(models.Model):
    _name = "medical.history"
    _description = "All Medical History"

    name = fields.Char(string="Diseases", required="True")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    treatment = fields.Char()
    sequelae = fields.Char()
    note = fields.Char(string="Note")
    patient_medical_id = fields.Many2one("patients.list")
