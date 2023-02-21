from odoo import models,fields

class MedicineList(models.Model):
    _name = "medicine.list"
    _description="List of medicine"
    
    name = fields.Char(required="True",string="Medicine")
    dosage_from = fields.Char()
    doses = fields.Char()
    note = fields.Char()
    