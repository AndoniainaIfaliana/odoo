# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GestionProfessor(models.Model):
     _name = 'gestion.professor'
#     _rec_name = 'f_name'

     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe = fields.Selection([('male','Male'),('female','Female')])
     idendity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     birthday = fields.Date('Birthday')
     start_date = fields.Date('Start date')
     email = fields.Char()
     phone = fields.Char()
     active = fields.Boolean()
     state = fields.Selection(selection=[ 
       ('draft', 'Draft'), 
       ('in_progress', 'En cours'), 
       ('cancel', 'Cancelled'), 
       ('done', 'Done'), 
     ], string='Status', required=True, readonly=True, copy=False, 
     tracking=True, default='draft')

     department_id = fields.Many2one(comodel_name='gestion.department')
     subject_ids = fields.One2many(comodel_name='gestion.subject', inverse_name='professor_id')
     classroom_ids = fields.Many2many(comodel_name='gestion.classroom',
                                      relation='prof_class_rel',
                                      column1='f_name',
                                      column2='name',)
     
     num_sub = fields.Integer(string='Number of subject', compute='comp_sub')
     num_cla = fields.Integer(string='Number of class', compute='comp_cla')

     def comp_sub(self):
          self.num_sub = len(self.subject_ids)

     def comp_cla(self):
          self.num_cla = len(self.classroom_ids)

     @api.constrains('start_date', 'birthday')
     def _check_date(self):
          if self.start_date > self.birthday:
               raise ValidationError("The birthday must be inferior than the registration date")

     def send_mail(self):
          self.ensure_one()
          template_id = self.env.ref('gestion.email_template_prof').id
          ctx = {
               'default_model': 'gestion.professor',
               'default_res_id': self.id,
               'default_use_template': bool(template_id),
               'default_template_id': template_id,
               'default_composition_mode': 'comment',
               'email_to': self.email,
          }
          return{
               'type': 'ir.actions.act_window',
               'view_type': 'form',
               'view_mode': 'form',
               'res_model': 'mail.compose.message',
               'target': 'new',
               'context': ctx,
          }