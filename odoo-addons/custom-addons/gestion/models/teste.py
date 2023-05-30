# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionTeste(models.Model):
     _name = 'gestion.teste'
     _rec_name = 'name'

     name = fields.Char()
     code = fields.Char()
