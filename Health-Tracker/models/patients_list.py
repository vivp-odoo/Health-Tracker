from odoo import api, models,fields

class PatientsList(models.Model):
    _name="patients.list"
    _description="Patients detail"
    
    name=fields.Char(required=True ,string="Patients Name")
    image = fields.Binary()
    phone=fields.Char(string="Phone")
    mobile=fields.Char(string="Mobile")
    street1=fields.Char()
    street2=fields.Char()
    zip=fields.Char()
    address=fields.Selection(string="Address",selection=[('own','patient'),('relative','Relative')])
    country = fields.Many2one("res.country",string="Country")
    state = fields.Many2one("res.country.state",string="State")
    email=fields.Char(string="E-mail")
    date=fields.Date(default = lambda self :fields.Date.today(), string="Registration Date")
    gender=fields.Selection(
        string = "Gender",
        selection =[('male','Male'),('female','Female')]
    )
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age" ,compute = "_compute_age")
    emergency_contact = fields.Char(string="Emegency Contact")
    medical_history_ids = fields.One2many("medical.history","patient_medical_id",string="Medical History")
    insurance = fields.Boolean()
    insurance_company = fields.Char()
    insurance_name = fields.Char()
    insurance_number = fields.Char()
    insurance_detail = fields.Char()
    insurance_validty = fields.Date()
    notes = fields.Char(string="Notes")
    contact_ids = fields.One2many("contacts.list","pat_id")
    active = fields.Boolean(default=True)
    
    @api.depends("dob")
    
    def _compute_age(self):
        for record in self: 
            if record.dob:
                record.age =  fields.Date.today().year - record.dob.year
            else :
                record.age = 0
    
