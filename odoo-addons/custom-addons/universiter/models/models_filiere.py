# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universiterFiliere(models.Model):
    _name = 'universiter.filiere'
    _rec_name = 'nom_filiere'

    id_filiere = fields.Integer(string='Code filière', required=True)
    nom_filiere = fields.Char(string='Nom filière', required=True)

    matiere_ids = fields.One2many(comodel_name='universiter.matiere', inverse_name='filiere_id')
    etudiant_ids = fields.One2many(comodel_name='universiter.etudiant', inverse_name='filiere_id')
    enseignant_ids = fields.One2many(comodel_name='universiter.enseignant', inverse_name='filiere_id')

    def create_filiere_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='filiere'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'id_filiere': {'type': 'integer'},
                    'nom_filiere': {'type': 'text'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='filiere', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universiterFiliere, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='filiere', body={
                'id_filiere': record.id_filiere,
                'nom_filiere': record.nom_filiere,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universiterFiliere, self).write(vals)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='filiere', body={
                'id_filiere': record.id_filiere,
                'nom_filiere': record.nom_filiere,
            }, id=record.id)
        return res
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        es = Elasticsearch(['localhost:9200'])
        if len(args) == 1 and args[0][0] == 'nom_filiere':
            query = args[0][2]
            search_body = {
                "query": {
                    "match": {
                        "nom_filiere": query
                    }
                }
            }
            result = es.search(index='filiere', body=search_body)
            record_ids = [r['_id'] for r in result['hits']['hits']]
            return super(universiterFiliere, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universiterFiliere, self).search(args, offset=offset, limit=limit, order=order, count=count)