# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bd(models.Model):
    _name = 'bd.depenses'
    _rec_name = 'id_depense'

    id_depense=fields.Char()
    cout_unitaire=fields.Char()
    nbr=fields.Char()
    date=fields.Date()
    commentaire=fields.Text()
    active = fields.Boolean()

    items_id = fields.Many2one(comodel_name = 'bd.items')
    respachat_ids = fields.One2many(comodel_name='bd.respachat', inverse_name='responsables_id')

    num_ra = fields.Integer(string='Nombre des responsables achats', compute='comp_ra')

    def comp_ra(self):
          self.num_ra = len(self.respachat_ids)
