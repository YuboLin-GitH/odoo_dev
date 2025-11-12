# -*- coding: utf-8 -*-

from odoo import models, fields, api


class genero(models.Model):
    _name = 'filmotecayubo.genero'
    _description = 'filmotecayubo.genero'


    name = fields.Char(string="Nombre", readonly = False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    esIntriga = fields.Boolean()
    esInfantil = fields.Boolean()
