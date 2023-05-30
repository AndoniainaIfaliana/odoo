# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bd(models.Model):
    _name = 'bd.responsables'
    _inherit = 'mail.thread'

    id_responsable=fields.Char()
    nom=fields.Char()
    commentaires=fields.Text()

    respachat_ids = fields.One2many(comodel_name='bd.respachat', inverse_name='depenses_id')

    num_ra = fields.Integer(string='Nombre des responsables achats', compute='comp_ra')

    def comp_ra(self):
          self.num_ra = len(self.respachat_ids)
 
    def name_get(self):
          result=[]
          for responsables in self:
               name = responsables.id_responsable + ' ' + '[' +responsables.nom + ']'
               result.append((responsables.id, name))
          return result
    
@api.onchange('respachat_ids')
def check_number_of_respachat(self):
      if len(self.respachat_ids) > 3:
            return {'warning': {
                  'title':'Warning',
                  'message':'Le nombre maximale des responsables achats est 3'
               }}