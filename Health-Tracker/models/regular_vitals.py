from odoo import models,fields

class RegularVitals(models.Model):
    _name = "regular.vitals"
    _description="Regular Vital check"
    
    
    blood_pressure = fields.Char(string="Blood Pressure")
    sugar = fields.Char(string="Sugar")
    oxygen_level = fields.Char(string="Oxygen Level")
    wieght = fields.Char(string="Weight")
    fever = fields.Char(string="Fever")
    pulse_rate = fields.Char(string="Pulse Rate")
    respiration_rate = fields.Char(string="Respiration Rate")
    note = fields.Char(required = True)
    