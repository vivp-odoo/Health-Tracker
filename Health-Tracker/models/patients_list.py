from odoo import models,fields

class PatientsList(models.Model):
    _name="patients.list"
    _description="Patients detail"
    
    name=fields.Char(required=True ,string="Patients Name")
    contact=fields.Char(required=True ,string="Phone no.")
    address=fields.Char(string="Address")
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
    
    