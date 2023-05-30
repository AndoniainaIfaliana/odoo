# -*- coding: utf-8 -*-

# from odoo import models, fields, api
# from elasticsearch import Elasticsearch


# class esearch(models.Model):
#     _name = 'esearch.teste'

#     nom_teste = fields.Char('Nom teste', required=True, compute='create_index')
     
#     def create_index():
#         es = Elasticsearch()
#         doc = {
#         "nom": "nom_teste",
#     # "l_name": "",
#     # "sexe": "",
#     # "idendity_card": "",
#     # "address": "",
#     # "birthday": "",
#     # "registration_date": "",
#     # "email": "",
#     # "phone": "",
#         }
#         es.indices.create(index='t', document=doc)
    
     
from odoo import models, fields, api
import requests

class teste(models.Model):  
    _name = 'esearch.teste'

    name = fields.Char('nom')
    description = fields.Text('description')

    def write(self, vals):
        res = super(teste, self).write(vals)
        if vals:
            index_name = 'lina'
            elastic_url = 'http://localhost:9200'
            for record in self:
                data = {
                    "name": record.name,
                    "description": record.description
                }
                r = requests.post(f"{elastic_url}/{index_name}/_doc", json=data)
                if r.status_code != requests.codes.ok:
                    r.raise_for_status()
        return res
