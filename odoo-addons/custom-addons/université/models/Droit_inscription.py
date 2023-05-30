# -*- coding: utf-8 -*-

from odoo import models, fields, api


class université(models.Model):
    _name = 'universite.droit'

    prix_droit_inscription = fields.Integer("Droit d'inscription")
    date_payement_droit_ins = fields.Datetime('Date payements')
    status_payement_droit_ins = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    