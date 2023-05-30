# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universitéClasse(models.Model):
    _name = 'universite.classes'
    _rec_name = 'nom_classe'

    code_classe = fields.Integer()
    nom_classe = fields.Char('Classe')
    filiere_id = fields.Many2one(comodel_name='universite.filieres', string='Filière')

    def create_classe_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='classe'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'code_classe': {'type': 'integer'},
                    'nom_classe': {'type': 'text'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='classe', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universitéClasse, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='classe', body={
                'code_classe': record.code_classe,
                'nom_classe': record.nom_classe,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universitéClasse, self).write(vals)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='classe', body={
                'code_classe': record.code_classe,
                'nom_classe': record.nom_classe,
            }, id=record.id)
        return res
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        es = Elasticsearch(['localhost:9200'])
        if len(args) == 1 and args[0][0] == 'nom_classe':
            query = args[0][2]
            search_body = {
                "query": {
                    "match": {
                        "nom_classe": query
                    }
                }
            }
            result = es.search(index='classe', body=search_body)
            record_ids = [r['_id'] for r in result['hits']['hits']]
            return super(universitéClasse, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universitéClasse, self).search(args, offset=offset, limit=limit, order=order, count=count)
