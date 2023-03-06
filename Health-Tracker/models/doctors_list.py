from odoo import api, models, fields


class DoctorsList(models.Model):
    _name = "doctors.list"
    _description = "list of doctors"

    name = fields.Char(required=True)
    image = fields.Binary()
    specialization = fields.Char(string="Specialization")
    qualification = fields.Char(string="Qualification")
    email = fields.Char(string="E-mail")
    contact = fields.Char(string="Phone No.")
    gender = fields.Selection(
        string="Gender", selection=[("male", "Male"), ("female", "Female")]
    )
    licence_number = fields.Char(string="License Number")
    address = fields.Char(string="Address")
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", readonly=False)
    notes = fields.Char(string="Notes")
    active = fields.Boolean(default=True)
    consulting_fees = fields.Integer(string="Consulting Fees")
    appointment_ids = fields.One2many("patients.appointment", "doctor_id")
    appointment_count = fields.Char(compute="_compute_appointment_count")

    @api.depends("dob")
    def _compute_age(self):
        if self.dob:
            self.age = fields.Date.today().year - self.dob.year
        else:
            self.age = 0

    _sql_constraints = [
        ("unqiue_licence", "unique(licence_number)", "Licence Number Must be Unique")
    ]

    @api.depends("appointment_ids")
    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.appointment_ids.search_count([])

    # def action_appointment_list(self):
    #     self.ensure_one()
    #     view = {
    #         "type": "ir.actions.act_window",
    #         "view_mode": "tree,form",
    #         "res_model": "patients.appointment",
    #         "name": "Models",
    #         "domain": [("doctor_id", "=", "active_id")],
    #     }
    #     return view
