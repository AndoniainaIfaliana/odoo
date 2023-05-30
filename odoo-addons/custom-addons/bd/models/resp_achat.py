# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bd(models.Model):
    _name = 'bd.respachat'

    nom_resp = fields.Char()
    responsables_id = fields.Many2one(comodel_name='bd.responsables')
    depenses_id = fields.Many2one(comodel_name='bd.depenses')