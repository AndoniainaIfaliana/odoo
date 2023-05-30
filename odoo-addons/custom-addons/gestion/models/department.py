# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionDepartment(models.Model):
     _name = 'gestion.department'
     _rec_name = 'name'

     name = fields.Char()
     code = fields.Char()

     subject_ids = fields.One2many(comodel_name='gestion.subject', inverse_name='department_id')
     student_ids = fields.One2many(comodel_name='gestion.student', inverse_name='department_id')
     professor_ids = fields.One2many(comodel_name='gestion.professor', inverse_name='department_id')

     num_sub = fields.Integer(srting='Number of subject', compute='comp_sub')
     num_stu = fields.Integer(string='Number of student', compute='comp_stu')
     num_prof = fields.Integer(string='Number of professor', compute='comp_prof')

     def comp_sub(self):
          self.num_sub = len(self.subject_ids)

     def comp_stu(self):
          self.num_stu = len(self.student_ids)
     
     def comp_prof(self):
          self.num_prof = len(self.professor_ids)