from odoo import api, models, fields, _
from odoo.exceptions import UserError
from odoo.tools.rendering_tools import relativedelta_proxy
from dateutil.relativedelta import relativedelta


class PatientsAppointment(models.Model):
    _name = "patients.appointment"
    _description = "Appointment for patients"

    _rec_name = "patient_name_id"
    patient_name_id = fields.Many2one(
        "patients.list", string="Patient Name", required=True
    )
    gender = fields.Selection(
        string="Gender",
        selection=[("male", "Male"), ("female", "Female")],
        related="patient_name_id.gender",
    )
    age = fields.Integer(related="patient_name_id.age", readonly=False)
    image = fields.Binary(compute="_compute_image", related="patient_name_id.image")
    contact = fields.Char(related="patient_name_id.phone", readonly=False)
    date = fields.Date(
        string="Appointment Date",
        default=lambda self: fields.Date.today() + relativedelta_proxy(days=1),
    )
    date_deadline = fields.Date(
        string="Appointment Deadline", compute="_compute_date_deadline"
    )
    doctor_id = fields.Many2one("doctors.list", required=True)
    consulting_fees = fields.Integer(
        related="doctor_id.consulting_fees", readonly=False
    )
    other_fees = fields.Integer(default=0)
    total_fees = fields.Integer(compute="_compute_total_fees")
    appointment_no = fields.Char(
        string="Appointment number",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: ("New"),
    )

    state = fields.Selection(
        string="Status",
        selection=[
            ("scheduled", "Scheduled"),
            ("confirmed", "Confirmed"),
            ("cancelled", "Cancelled"),
        ],
        default="scheduled",
    )
    reason = fields.Char(string="Reason")
    notes = fields.Char(string="Notes")
    medicine_prescribed = fields.Many2many("medicine.list", string="Medicines")
    next_appointment = fields.Date(string="Next Appointment")
    treatment = fields.Char()
    next_step = fields.Char()
    admit = fields.Boolean(string="Admitted")
    active = fields.Boolean(default=True)
    vital_ids = fields.One2many("regular.vitals", "patient_id", string="Vitals")

    @api.model
    def create(self, vals_list):
        if vals_list.get("appointment_no", ("New")) == ("New"):
            vals_list["appointment_no"] = self.env["ir.sequence"].next_by_code(
                "patients.appointment"
            ) or ("New")
        return super(PatientsAppointment, self).create(vals_list)

    @api.depends("date")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.date + relativedelta(days=7)

    @api.depends("total_fees", "other_fees")
    def _compute_total_fees(self):

        for record in self:
            record.total_fees = record.consulting_fees + record.other_fees

    def action_accept(self):
        for rec in self:
            rec.state = "confirmed"
            if rec.next_appointment:
                if rec.next_appointment <= rec.date:
                    raise UserError(
                        _(
                            "What the hell !!!!! You need to select next appointment greater than appointment date"
                        )
                    )
        return True

    def action_refuse(self):
        for rec in self:
            rec.state = "cancelled"
        return True
