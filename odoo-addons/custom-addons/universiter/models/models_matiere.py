# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universiterMatiere(models.Model):
    _name = 'universiter.matiere'
    _rec_name = 'nom_matiere'
    
    id_matiere = fields.Integer(string='Code matière', required=True)
    nom_matiere = fields.Char(string='Nom matière', required=True)
    
    filiere_id = fields.Many2one(comodel_name='universiter.filiere', string='Filière')
    etudiant_id = fields.Many2one(comodel_name='universiter.etudiant', string='Etudiant')
    enseignant_ids = fields.One2many(comodel_name='universiter.enseignant', inverse_name='matiere_id')

    def create_matiere_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='matiere'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'id_matiere': {'type': 'integer'},
                    'nom_matiere': {'type': 'text'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='matiere', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universiterMatiere, self).create(vals_list)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='matiere', body={
                'id_matiere': record.id_matiere,
                'nom_matiere': record.nom_matiere,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universiterMatiere, self).write(vals)
        # Envoye les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='matiere', body={
                'id_matiere': record.id_matiere,
                'nom_matiere': record.nom_matiere,
            }, id=record.id)
        return res
    
    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        es = Elasticsearch(['localhost:9200'])
        if len(args) == 1 and args[0][0] == 'nom_matiere':
            query = args[0][2]
            search_body = {
                "query": {
                    "match": {
                        "nom_matiere": query
                    }
                }
            }
            result = es.search(index='matiere', body=search_body)
            record_ids = [r['_id'] for r in result['hits']['hits']]
            return super(universiterMatiere, self).search([('id', 'in', record_ids)], offset=offset, limit=limit, order=order, count=count)
        else:
            return super(universiterMatiere, self).search(args, offset=offset, limit=limit, order=order, count=count)