from odoo import models,fields

class ContactsList(models.Model):
    _name ="contacts.list"
    _description = "Contacts"
    
    _rec_name = "contact_person"
    contact_person = fields.Selection(
        string = "contact",
        selection=[('own','Patient'),('relative','Relative')]
    )
    
    street1 = fields.Char()
    street2 = fields.Char()
    city = fields.Char()
    state = fields.Many2one("res.country.state")
    country = fields.Many2one("res.country")
    zip = fields.Char()
    pat_id = fields.Many2one("patients.list")



