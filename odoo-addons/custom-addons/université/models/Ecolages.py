# -*- coding: utf-8 -*-

from odoo import models, fields, api


class université(models.Model):
    _name = 'universite.ecolages'
    _rec_name = 'etudiant_id'
    
    prix_premier_tranche = fields.Integer('Premier tranche (Ar)')
    date_payement_1e_t = fields.Date('Date payement 1er tranche')
    status_payement_1e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    prix_deuxieme_tranche = fields.Integer('Deuxième tranche (Ar)')
    date_payement_2e_t = fields.Date('Date payement 2ème tranche')
    status_payement_2e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    prix_troisieme_tranche = fields.Integer('Troisième tranche (Ar)')
    date_payement_3e_t = fields.Date('Date payement 3ème tranche')
    status_payement_3e_t = fields.Selection([('non payé','Non payé'),('payé','Payé')], string='Status')
    etudiant_id = fields.Many2one(comodel_name='universite.etudiants', string='N° Matricule étudiant', required=True)
    filiere_id = fields.Many2one(comodel_name='universite.filieres', string='Filière')