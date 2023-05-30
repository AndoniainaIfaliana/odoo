# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universiterEtudiant(models.Model):
    _name = 'universiter.etudiant'
    _rec_name = 'matricule_etudiant'
    

    matricule_etudiant = fields.Integer(string='N° Matricule', required=True)
    nom_etudiant = fields.Char('Nom', required=True)
    prenom_etudiant = fields.Char('Prenom', required=True)
    sexe = fields.Selection([('masculin','Masculin'),('féminin','Féminin')], required=True)
    date_naissance = fields.Date('Date de naissance', required=True)
    lieu_naissance = fields.Char('Lieu de naissance', required=True)
    date_inscription = fields.Datetime("Date d'inscription", default = fields.Datetime.now, required=True)
    adresse = fields.Char("Adresse", required=True)
    mail = fields.Char('Email')
    num = fields.Integer('Tel', required=True)
    niveaux = fields.Selection([('licence 1','Licence 1'),('licence 2','Licence 2'),('licence 3','Licence 3'),('master 1','Master 1'),('master 2','Master 2')], default = 'licence 1', required=True)

    filiere_id = fields.Many2one(comodel_name='universiter.filiere', string='Filière')
    classe_id = fields.Many2one(comodel_name='universiter.classe', string='Classe')
    matiere_ids = fields.One2many(comodel_name='universiter.matiere', inverse_name='etudiant_id')

    def create_etudiant_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='etudiant'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'matricule_etudiant': {'type': 'integer'},
                    'nom_etudiant': {'type': 'text'},
                    'prenom_etudiant': {'type': 'text'},
                    'sexe': {'type': 'text'},
                    'date_naissance': {'type': 'text'},
                    'lieu_naissance': {'type': 'text'},
                    'date_inscription': {'type': 'text'},
                    'adresse': {'type': 'text'},
                    'mail': {'type': 'text'},
                    'num': {'type': 'integer'},
                    'niveaux': {'type': 'text'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='etudiant', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universiterEtudiant, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='etudiant', body={
                'matricule_etudiant': record.matricule_etudiant,
                'nom_etudiant': record.nom_etudiant,
                'prenom_etudiant': record.prenom_etudiant,
                'sexe': record.sexe,
                'date_naissance': record.date_naissance,
                'lieu_naissance': record.lieu_naissance,
                'date_inscription': record.date_inscription,
                'adresse': record.adresse,
                'mail': record.mail,
                'num': record.num,
                'niveaux': record.niveaux,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universiterEtudiant, self).write(vals)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='etudiant', body={
                'matricule_etudiant': record.matricule_etudiant,
                'nom_etudiant': record.nom_etudiant,
                'prenom_etudiant': record.prenom_etudiant,
                'sexe': record.sexe,
                'date_naissance': record.date_naissance,
                'lieu_naissance': record.lieu_naissance,
                'date_inscription': record.date_inscription,
                'adresse': record.adresse,
                'mail': record.mail,
                'num': record.num,
                'niveaux': record.niveaux,
            }, id=record.id)
        return res
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        es = Elasticsearch(['localhost:9200'])
        if len(args) == 1:
            if args[0][0] == 'prenom_etudiant':
                query = args[0][2]
                search_body = {
                    "query": {
                        "match": {
                            "prenom_etudiant": query
                        }
                    }
                }
            elif args[0][0] == 'niveau':
                query = args[0][2]
                search_body = {
                    "query": {
                        "match": {
                            "niveaux": query
                        }
                    }
                }
            else:
                return super(universiterEtudiant, self).search(args, offset=offset, limit=limit, order=order, count=count)

            result = es.search(index='etudiant', body=search_body)
            record_ids = [r['_id'] for r in result['hits']['hits']]
            return super(universiterEtudiant, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universiterEtudiant, self).search(args, offset=offset, limit=limit, order=order, count=count)
