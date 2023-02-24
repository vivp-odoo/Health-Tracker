from odoo import api, models,fields
from odoo.tools.rendering_tools import relativedelta_proxy
from dateutil.relativedelta import relativedelta

class PatientsAppointment(models.Model):
    _name = "patients.appointment"
    _description = "Appointment for patients"
    
    _rec_name = "patient_name"
    patient_name = fields.Many2one("patients.list",string="Patient Name")
    image = fields.Binary(compute = "_compute_image")
    contact = fields.Integer()
    date = fields.Date(string="Appointment Date",default = lambda self : fields.Date.today() + relativedelta_proxy(days=1))
    date_deadline = fields.Date(string="Appointment Deadline", compute = "_compute_date_deadline")
    doctor = fields.Many2one("doctors.list")
    consulting_fees = fields.Char(default = 500)
    state = fields.Selection(
        string = "Status",
        selection = [('scheduled','Scheduled'),('confirmed','Confirmed'),('cancelled','Cancelled')],
        default="scheduled"
    )
    reason = fields.Char(string="Reason")
    notes = fields.Char(string="Notes")
    medicine_prescribed = fields.Many2many("medicine.list" , string = "Medicines")
    next_appointment = fields.Date(string="Next Appointment")
    treatment = fields.Char()
    next_step = fields.Char()
    admit = fields.Boolean(string="Admitted")
    active = fields.Boolean(default = True)
    vital_ids = fields.One2many( "regular.vitals" ,"patient_id", string="Vitals")

    
    @api.depends("date")
     
    def _compute_date_deadline(self):
         for record in self:
             record.date_deadline = record.date + relativedelta(days = 7)
             
    @api.depends("patient_name")
    
    def _compute_image(self):
        if self.image == 0:
            self.image = self.patient_name.image
        else:
            self.image = 0

    def action_accept(self):
        for rec in self:
            rec.state = "confirmed"
        return True
    
    def action_refuse(self):
        for rec in self:
            rec.state = "cancelled"
        return True