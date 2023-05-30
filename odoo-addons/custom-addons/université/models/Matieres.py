# -*- coding: utf-8 -*-

from odoo import models, fields, api


class universitéMatiere(models.Model):
    _name = 'universite.matieres'
    _rec_name = 'nom_matiere'

    code_matiere = fields.Integer()
    nom_matiere = fields.Char('Matière')
    prof_id = fields.Many2one(comodel_name='universite.prof', string='Enseignant')
    etudiant_id = fields.Many2one(comodel_name='universite.etudiants', string='Etudiant')
    filiere_id = fields.Many2one(comodel_name='universite.filieres', string='Filière')