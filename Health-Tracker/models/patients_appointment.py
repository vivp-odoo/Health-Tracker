from odoo import models,fields
from odoo.tools.rendering_tools import relativedelta_proxy

class PatientsAppointment(models.Model):
    _name = "patients.appointment"
    _description = "Appointment for patients"
    
    _rec_name = "patient_name"
    patient_name = fields.Many2one("patients.list",string="Patient Name")
    contact = fields.Char()
    date = fields.Date(string="Appointment Date",default = lambda self : fields.Date.today() + relativedelta_proxy(days=1))
    doctor = fields.Many2one("doctors.list")
    consulting_fees = fields.Char()
    status = fields.Selection(
        string = "Status",
        selection = [('scheduled','Scheduled'),('confirmed','Confirmed'),('cancelled','Cancelled')]
    )
    reason = fields.Char(string="Reason")
    notes = fields.Char(string="Notes")
    medicine_prescribed = fields.Many2many("medicine.list" , string = "Medicines")
    next_appointment = fields.Char(string="Next Appointment")
    Treatment = fields.Char()
    next_step = fields.Char()
    admit = fields.Boolean(string="Admitted")
    # vitals = fields.One2many(string="Vitals")
    
    
     