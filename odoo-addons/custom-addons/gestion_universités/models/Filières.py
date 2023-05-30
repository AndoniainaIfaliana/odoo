# -*- coding: utf-8 -*-

from odoo import models, fields, api


class gestion_universités(models.Model):
    _name = 'gestion_universités.Filières'

    id_filières = fields.Integer()
    nom_filière = fields.Char()