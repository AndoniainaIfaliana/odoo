# -*- coding: utf-8 -*-

from odoo import models, fields, api


class universitéProf(models.Model):
    _name = 'universite.prof'
    _rec_name = 'matricule_enseignant'

    matricule_enseignant = fields.Integer(string='N° Matricule', required=True)
    nom_enseignant = fields.Char('Nom', required=True)
    prenom_enseignant = fields.Char('Prenom', required=True)
    sexe = fields.Selection([('masculin','Masculin'),('féminin','Féminin')])
    date_naissance_enseignant = fields.Date('Date de naissance')
    lieu_naissance_enseignant = fields.Char('Lieu de naissance')
    date_debut = fields.Datetime("Date de début", default=fields.Datetime.now)
    adresse_enseignant = fields.Char("Adresse")
    mail_enseignant = fields.Char('Email')
    num_enseignant = fields.Integer('Tel')
    etudiant_id = fields.Many2one(comodel_name='universite.etudiants', string='Etudiant')
    filiere_id = fields.Many2one(comodel_name='universite.filieres', string='Filière')
    matiere_ids = fields.One2many(comodel_name='universite.matieres', inverse_name='prof_id')
    filiere_ids = fields.One2many(comodel_name='universite.filieres', inverse_name='prof_id')
