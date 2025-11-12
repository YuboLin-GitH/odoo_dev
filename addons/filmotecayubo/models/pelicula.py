# -*- coding: utf-8 -*-

from odoo import models, fields, api


class pelicula(models.Model):
    _name = 'filmotecayubo.pelicula'
    _description = 'filmotecayubo.pelicula'


    name = fields.Char(string="Nombre", readonly = False, required=True, help="Introduzca el nombre")
    description = fields.Text()
    film_date = fields.Date()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_spanish = fields.Boolean()
    imagen = fields.Binary(string="Imagen", help="Suba la imagen de la película")
    lenguage = fields.Selection([('es', 'Español'),
                                ('en', 'Inglés'),
                                ('fr', 'Francés'),
                                ('de', 'Alemán')],
                                 string="Lenguaje",
                                    default='es',
                                    help="Seleccione el lenguaje de la película")
    opinion = fields.Selection([('0', 'mala'),
                               ('1', 'regular'),
                                 ('2', 'buena')],
                                  string="Opinion",
                                        default='1',
                                        help="Seleccione la opinión sobre la película")
    color = fields.Selection([('bn', 'Blanco y negro'),
                              ('cl', 'Color')],
                                string="Color",
                                    default='cl',
                                    help="Seleccione la color la película")
  