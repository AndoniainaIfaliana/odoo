# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionSubject(models.Model):
     _name = 'gestion.subject'
     _rec_name = 'name'

     name = fields.Char()
     code = fields.Char()

     department_id = fields.Many2one(comodel_name='gestion.department')
     student_id = fields.Many2one(comodel_name='gestion.student')
     professor_id = fields.Many2one(comodel_name='gestion.professor')