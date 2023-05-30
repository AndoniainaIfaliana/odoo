# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from elasticsearch import Elasticsearch

es = Elasticsearch()

class GestionStudent(models.Model):
     _name = 'gestion.student'

     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     idendity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     birthday = fields.Date('Birthday')
     registration_date = fields.Date('Registration date')
     email = fields.Char()
     phone = fields.Char()
     state = fields.Selection([ 
       ('l1','Level1'), 
       ('l2','Level2'), 
       ('l3','Level3'), 
       ('finish','Finished'), 
     ], required=True, readonly=True, default='l1')

     department_id = fields.Many2one(comodel_name='gestion.department')
     classroom_id = fields.Many2one(comodel_name='gestion.classroom')
     subject_ids = fields.One2many(comodel_name='gestion.subject', inverse_name='student_id')

     num_sub = fields.Integer(string='Number of subject', compute='comp_sub')

     _doc = {
          "f_name": f_name,
          "l_name": l_name,
          "sexe": sexe,
          "idendity_card": idendity_card,
          "address": address,
          "birthday": birthday,
          "registration_date": registration_date,
          "email": email,
          "phone": phone,
     }     

     def comp_sub(self):
          self.num_sub = len(self.subject_ids)

     def name_get(self):
          result=[]
          for student in self:
               name = student.f_name + ' ' + student.l_name
               result.append((student.id, name))
          return result
     
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