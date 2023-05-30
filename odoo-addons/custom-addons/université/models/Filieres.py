# -*- coding: utf-8 -*-

from odoo import models, fields, api
from elasticsearch import Elasticsearch

class universitéFiliere(models.Model):
    _name = 'universite.filieres'
    _rec_name = 'nom_filiere'

    code_filiere = fields.Integer()
    nom_filiere = fields.Char('Filière')
    prof_id = fields.Many2one(comodel_name='universite.prof')
    matiere_ids = fields.One2many(comodel_name='universite.matieres', inverse_name='filiere_id')
    enseignant_ids = fields.One2many(comodel_name='universite.prof', inverse_name='filiere_id')

    def create_filiere_index(self):
        # Configurer la connexion à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        # Vérifier si l'index existe
        if not es.indices.exists(index='filiere'):
            # Définir le mapping pour les champs indexés
            mapping = {
                'properties': {
                    'code_filiere': {'type': 'integer'},
                    'nom_filiere': {'type': 'text'},
                }
            }
            # Créer l'index avec le mapping
            es.indices.create(index='filiere', body={'mappings': mapping})

    @api.model_create_multi
    @api.model
    def create(self, vals_list):
        res = super(universitéFiliere, self).create(vals_list)
        # Envoyer les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in res:
            es.index(index='filiere', body={
                'code_filiere': record.code_filiere,
                'nom_filiere': record.nom_filiere,
            }, id=record.id)
        return res

    def write(self, vals):
        res = super(universitéFiliere, self).write(vals)
        # Envoyer les données à Elasticsearch
        es = Elasticsearch(['localhost:9200'])
        for record in self:
            es.index(index='filiere', body={
                'code_filiere': record.code_filiere,
                'nom_filiere': record.nom_filiere,
            }, id=record.id)
        return res
