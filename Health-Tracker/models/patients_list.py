from odoo import models,fields

class PatientsList(models.Model):
    _name="patients.list"
    _description="Patients detail"
    
    name=fields.Char(required=True ,string="Patients Name")
    contact=fields.Char(required=True ,string="Phone no.")
    address=fields.Char(string="Address")
    email=fields.Char(string="E-mail")
    date=fields.Date(default = lambda self :fields.Date.today())
    gender=fields.Selection(
        string = "Gender",
        selection =[('male','Male'),('female','Female')]
    )
    
    