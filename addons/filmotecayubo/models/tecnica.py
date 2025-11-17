# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tecnica(models.Model):
    _name = 'filmotecayubo.tecnica'
    _description = 'filmotecayubo.tecnica'


    name = fields.Char(string="Nombre")
    description = fields.Text(string="Descripción")
    photo = fields.Binary(string="Imagen")


    peliculas_id= fields.Many2many(comodel_name ="filmotecayubo.pelicula",
                                  relation = "tecnicas_peliculas",
                                  columna1 = "tecnica_id",
                                  columna2 = "pelicula_id",
                                  string = "Películas")