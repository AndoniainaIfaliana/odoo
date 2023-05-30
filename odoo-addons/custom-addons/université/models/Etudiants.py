# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch


class universitéEtudiant(models.Model):
    _name = 'universite.etudiants'
    _rec_name = 'matricule_etudiant'

    matricule_etudiant = fields.Integer(string='N° Matricule', required=True)
    nom_etudiant = fields.Char('Nom')
    prenom_etudiant = fields.Char('Prenom')
    sexe = fields.Selection([('masculin','Masculin'),('féminin','Féminin')])
    date_naissance = fields.Date('Date de naissance')
    lieu_naissance = fields.Char('Lieu de naissance')
    date_inscription = fields.Datetime("Date d'inscription")
    adresse = fields.Char("Adresse")
    mail = fields.Char('Email')
    num = fields.Integer('Tel')
    niveaux = fields.Selection([('licence 1','Licence 1'),('licence 2','Licence 2'),('licence 3','Licence 3'),('master 1','Master 1'),('master 2','Master 2')])
    filiere_id = fields.Many2one(comodel_name='universite.filieres', string='Filière')
    matiere_ids = fields.One2many(comodel_name='universite.matieres', inverse_name='etudiant_id')
    enseignant_ids = fields.One2many(comodel_name='universite.prof', inverse_name='etudiant_id')


    # def name_get(self):
    #       result=[]
    #       for student in self:
    #            name = self.nom_etudiant + ' ' + self.prenom_etudiant
    #            result.append((student.id, name))
    #       return result

    # _doc = {
    #     "matricule_etudiant": matricule_etudiant,
    #     "nom_etudiant": nom_etudiant,
    #     "prenom_etudiant": prenom_etudiant,
    #     "sexe": sexe,
    #     "date_naissance": date_naissance,
    #     "lieu_naissance": lieu_naissance,
    #     "date_inscription": date_inscription,
    #     "adresse": adresse,
    #     "mail": mail,
    #     "num": num,
    # }

    # def create(self, vals_list):
    #     es.index(index="etudiant", id=1, document=self._doc)
    #     return super().create(vals_list)

    # def search(self):
    #     res = es.search(index="etudiant", query={"match_all": {}})
    #     print("Got %d Hits:" % res['hits']['total']['value'])