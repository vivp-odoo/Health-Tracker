from odoo import models,fields

class PatientsList(models.Model):
    _name="patients.list"
    _description="Patients detail"
    
    name=fields.Char(required=True ,string="Patients Name")
    phone=fields.Char(string="Phone")
    mobile=fields.Char(string="Mobile")
    street1=fields.Char()
    street2=fields.Char()
    zip=fields.Char()
    address=fields.Char(string="Address")
    country = fields.Many2one("res.country",string="Country")
    state = fields.Many2one("res.country.state",string="State")
    email=fields.Char(string="E-mail")
    date=fields.Date(default = lambda self :fields.Date.today(), string="Registration Date")
    gender=fields.Selection(
        string = "Gender",
        selection =[('male','Male'),('female','Female')]
    )
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age")
    emergency_contact = fields.Char(string="Emegency Contact")
    medical_history = fields.Char(string="Medical History")
    insurance = fields.Char(string="Insurance")
    notes = fields.Char(string="Notes")
    contact_ids = fields.One2many("contacts.list","pat_id")
    