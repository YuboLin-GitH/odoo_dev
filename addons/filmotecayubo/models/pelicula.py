# -*- coding: utf-8 -*-

from odoo import models, fields, api


class filmotecayubo(models.Model):
    _name = 'filmotecayubo.pelicula'
    _description = 'filmotecayubo.pelicula'

    name = fields.Char(string="Nombre", readonly =False, required=True, help="Nombre de la pelicula")
    description = fields.Text()
    film_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_spanish = fields.Boolean()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

