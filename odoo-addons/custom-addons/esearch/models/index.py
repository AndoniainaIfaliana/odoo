# -*- coding: utf-8 -*-

# from odoo import models, fields, api
# from elasticsearch import Elasticsearch


# class esearch(models.Model):
#      _name = 'esearch.index'


#      nom_index = fields.Char(string='Nom index', required=True)
#      description_index = fields.Text(string='Description index')

#      def create_index(self):
#         es = Elasticsearch()
#         index_name = self.nom_index.lower().replace('.', '_').replace(',', '_')
#         es.indices.create(index=index_name)
     
#      @api.on_save('index_field')
#      def create_index_on_save(self):
#         self.create_index()

     # def delete_index(self):
     #    es = Elasticsearch()
     #    for record in self:
     #        nom_index = self.nom_index.lower().replace('.', '_').replace(',', '_')
     #        if es.indices.exists(index=nom_index):
     #            es.indices.delete(index=nom_index)


from odoo import models, fields, api
from elasticsearch import Elasticsearch, exceptions


class esearch(models.Model):
    _name = 'esearch.index'
    _import = False

    nom_index = fields.Char(string='Nom index', required=True)
    description_index = fields.Text(string='Description index')

    def create_index(self):
        
        es = Elasticsearch()
        index_name = self.nom_index.lower().replace('.', '_').replace(',', '_')
        if es.indices.exists(index_name):
            return 'Index already exists'
        else:
            es.indices.create(index=index_name)
            return 'Index created successfully'

    @api.model
    def create(self, vals):
        res = super(esearch, self).create(vals)
        res.create_index()
        return res


    def write(self, vals):
        res = super(esearch, self).write(vals)
        for record in self:
            record.create_index()
        return res
