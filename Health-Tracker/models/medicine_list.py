from odoo import models,fields

class MedicineList(models.Model):
    _name="medicine.list"
    _description="List of medicine"
    
    name = fields.Char(required="True" ,copy=False)
    dosage_from = fields.Char()
    doses = fields.Char()
    note = fields.Char()
    color = fields.Integer(string="color")

    _sql_constraints = [
        ('unique_name','unique(name)','Medicine name must me unique')
    ]
    