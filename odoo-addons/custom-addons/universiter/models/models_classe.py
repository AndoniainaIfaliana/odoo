# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universiterClasse(models.Model):
    _name = 'universiter.classe'
    _rec_name = 'nom_classe'
    
    code_classe = fields.Integer(string='Code classe', required=True)
    nom_classe = fields.Char(string='Nom classe', required=True)

    etudiant_ids = fields.One2many(comodel_name='universiter.etudiant', inverse_name='classe_id')

    enseignant_ids = fields.Many2many(comodel_name='universiter.enseignant',
                                      relation='class_ens_rel',
                                      column1='nom_classe',
                                      column2='prenom_enseignant')
    
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
        res = super(universiterClasse, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='classe', body={
                'code_classe': record.code_classe,
                'nom_classe': record.nom_classe,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universiterClasse, self).write(vals)
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
            return super(universiterClasse, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universiterClasse, self).search(args, offset=offset, limit=limit, order=order, count=count)
