# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionClassroom(models.Model):
     _name = 'gestion.classroom'
     _inherit = 'mail.thread'
     _rec_name = 'name'

     name = fields.Char(searchable=True)
     code = fields.Char()

     student_ids = fields.One2many(comodel_name='gestion.student', inverse_name='classroom_id')
     professor_ids = fields.Many2many(comodel_name='gestion.professor',
                                      relation='class_prof_rel',
                                      column1='name',
                                      column2='f_name')

     num_stu = fields.Integer(string='Number of student', compute='comp_stu')
     num_prof = fields.Integer(string='Number of professor', compute='comp_prof')

     def comp_stu(self):
          self.num_stu = len(self.student_ids)
     
     def comp_prof(self):
          self.num_prof = len(self.professor_ids)

          @api.onchange('professor_ids')
          def check_number_of_professors(self):
               if len(self.professor_ids) > 3:
                    return {'warning': {
                         'title':'Warning',
                         'message':'The number of professors must be less than 3'
                    }}
     