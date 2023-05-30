# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universiterEnseignant(models.Model):
    _name = 'universiter.enseignant'
    _rec_name = 'matricule_enseignant'
    
    matricule_enseignant = fields.Integer(string='N° Matricule', required=True)
    nom_enseignant = fields.Char('Nom', required=True)
    prenom_enseignant = fields.Char('Prenom', required=True)
    sexe = fields.Selection([('masculin','Masculin'),('féminin','Féminin')], required=True)
    date_naissance_enseignant = fields.Date('Date de naissance', required=True)
    lieu_naissance_enseignant = fields.Char('Lieu de naissance', required=True)
    date_debut = fields.Datetime("Date de début", default=fields.Datetime.now, required=True)
    adresse_enseignant = fields.Char("Adresse", required=True)
    mail_enseignant = fields.Char('Email')
    num_enseignant = fields.Integer('Tel', required=True)

    filiere_id = fields.Many2one(comodel_name='universiter.filiere', string='Filière enseigné')
    matiere_id = fields.Many2one(comodel_name='universiter.matiere', string='Matière enseigné')

    enseignant_ids = fields.Many2many(comodel_name='universiter.classe',
                                      relation='ens_class_rel',
                                      column1='prenom_enseignant',
                                      column2='nom_classe')

    def create_ensignant_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='enseignant'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'matricule_enseignant': {'type': 'integer'},
                    'nom_enseignant': {'type': 'text'},
                    'prenom_enseignant': {'type': 'text'},
                    'sexe': {'type': 'text'},
                    'date_naissance_enseignant': {'type': 'text'},
                    'lieu_naissance_enseignant': {'type': 'text'},
                    'date_debut': {'type': 'text'},
                    'adresse_enseignant': {'type': 'text'},
                    'mail_enseignant': {'type': 'text'},
                    'num_enseignant': {'type': 'integer'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='enseignant', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universiterEnseignant, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='enseignant', body={
                'matricule_enseignant': record.matricule_enseignant,
                'nom_enseignant': record.nom_enseignant,
                'prenom_enseignant': record.prenom_enseignant,
                'sexe': record.sexe,
                'date_naissance_enseignant': record.date_naissance_enseignant,
                'lieu_naissance_enseignant': record.lieu_naissance_enseignant,
                'date_debut': record.date_debut,
                'adresse_enseignant': record.adresse_enseignant,
                'mail_enseignant': record.mail_enseignant,
                'num_enseignant': record.num_enseignant,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universiterEnseignant, self).write(vals)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='enseignant', body={
                'matricule_enseignant': record.matricule_enseignant,
                'nom_enseignant': record.nom_enseignant,
                'prenom_enseignant': record.prenom_enseignant,
                'sexe': record.sexe,
                'date_naissance_enseignant': record.date_naissance_enseignant,
                'lieu_naissance_enseignant': record.lieu_naissance_enseignant,
                'date_debut': record.date_debut,
                'adresse_enseignant': record.adresse_enseignant,
                'mail_enseignant': record.mail_enseignant,
                'num_enseignant': record.num_enseignant,
            }, id=record.id)
        return res
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        es = Elasticsearch(['localhost:9200'])
        if len(args) == 1:
            if args[0][0] == 'prenom_enseignant':
                query = args[0][2]
                search_body = {
                    "query": {
                        "match": {
                            "prenom_enseignant": query
                        }
                    }
                }
            elif args[0][0] == 'matricule_enseignant':
                query = args[0][2]
                search_body = {
                    "query": {
                        "match": {
                            "matricule_enseignant": query
                        }
                    }
                }
            else:
                return super(universiterEnseignant, self).search(args, offset=offset, limit=limit, order=order, count=count)

            result = es.search(index='enseignant', body=search_body)
            record_ids = [r['_id'] for r in result['hits']['hits']]
            return super(universiterEnseignant, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universiterEnseignant, self).search(args, offset=offset, limit=limit, order=order, count=count)
