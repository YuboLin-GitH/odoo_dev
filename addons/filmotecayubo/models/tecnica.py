# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tecnica(models.Model):
    _name = 'filmotecayubo.tecnica'
    _description = 'filmotecayubo.tecnica'


    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    photo = fields.Binary(string="Imagen")


    