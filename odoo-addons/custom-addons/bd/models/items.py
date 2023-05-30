# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class bd(models.Model):
    _name = 'bd.items'
    _rec_name = 'id_item'

    id_item=fields.Char()
    item=fields.Char()
    commentaire=fields.Text()

    state = fields.Selection([ 
       ('l1','Level1'), 
       ('l2','Level2'), 
       ('l3','Level3'), 
       ('finish','Finished'), 
     ], required=True, readonly=True, default='l1')

    depenses_ids = fields.One2many(comodel_name='bd.depenses', inverse_name='items_id')

    num_dep = fields.Integer(string='Nombre des depenses', compute='comp_dep')

    def comp_dep(self):
          self.num_dep = len(self.depenses_ids)

    def next_level(self):
          if self.state == 'l1':
               return self.write({'state': 'l2'})
          elif self.state == 'l2':
               return self.write({'state': 'l3'})
          elif self.state == 'l3':
               return self.write({'state': 'finish'})
          elif self.state == 'finish':
                    raise ValidationError("This student has already finished his courses!")
          
    def prev_level(self):
          if self.state == 'finish':
               return self.write({'state': 'l3'})
          elif self.state == 'l3':
               return self.write({'state': 'l2'})
          elif self.state == 'l2':
               return self.write({'state': 'l1'})
          elif self.state == 'l1':
                    raise ValidationError("Niveau L1 est le plus bas!!")