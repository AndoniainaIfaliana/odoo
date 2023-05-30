# -*- coding: utf-8 -*-

from odoo import models, fields, api

class universiterEcolage(models.Model):
    _name = 'universiter.ecolage'
    _rec_name = 'prenom_etudiant'
    
    etudiant_id = fields.Many2one(comodel_name='universiter.etudiant', string='N° Matricule', required=True)
    prenom_etudiant = fields.Char(related='etudiant_id.prenom_etudiant', string='Etudiant')
    prix_premier_tranche = fields.Integer('Premier tranche (Ar)')
    date_payement_1e_t = fields.Date('Date payement 1er tranche', default = fields.Datetime.now)
    status_payement_1e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    prix_deuxieme_tranche = fields.Integer('Deuxième tranche (Ar)')
    date_payement_2e_t = fields.Date('Date payement 2ème tranche', default = fields.Datetime.now)
    status_payement_2e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    prix_troisieme_tranche = fields.Integer('Troisième tranche (Ar)')
    date_payement_3e_t = fields.Date('Date payement 3ème tranche', default = fields.Datetime.now)
    status_payement_3e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')