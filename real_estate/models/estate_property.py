# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class EstateProperty(models.Model):
     _name = 'estate.property'
     _description='Estate property'
     
     name                = fields.Char(string='Name')
     postcode            = fields.Char('Code postal')
     date_availability   = fields.Date("Date de validité")
     expected_price      = fields.Float('Prix prévu')
     selling_price       = fields.Float("Prix d'achat")#fields.Monetary(currency_field= "currency_id",string="Prix d'achat")
     bedrooms            = fields.Integer("Nombre de chambre")
     living_area         = fields.Integer("Surface habitable")
     facades             = fields.Integer("Nombre de facades")
     garage              = fields.Boolean("Garage")
     garden              = fields.Boolean("Avec garage")
     garden_area         = fields.Integer("Surface Garage")
     garden_orientation  = fields.Char("Orientation de jardin")
     description         = fields.Text('Description')    
     active              = fields.Boolean("Active",default=True) 
     state               = fields.Selection(
        selection=[
            ('optional', 'Optional'),
            ('mandatory', 'Mandatory'),
            ('unavailable', 'Unavailable'),
        ],
        string="State",
        required=True,
        default='optional',
        readonly=False,
    )