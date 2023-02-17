from odoo import models,fields

class DoctorsList(models.Model):
    _name = "doctors.list"
    _description = "list of doctors"
    

    name = fields.Char(required=True)
    specialization = fields.Char(string="Specialization")
    qualification = fields.Char(string="Qualification")
    email = fields.Char(string="E-mail")
    contact = fields.Char(string="Phone No.")
    gender = fields.Selection(
        string="Gender",
        selection=[("male","Male"),("female","Female")]
    )
    licencse_number = fields.Char(string="License Number")
    address = fields.Char(string="Address")
    dob = fields.Date(string="Date Of Birth")
    age = fields.Integer(string="Age")
    notes = fields.Char(string="Notes")
    
    
    