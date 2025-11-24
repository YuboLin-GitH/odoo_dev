# -*- coding: utf-8 -*-

import datetime
from odoo import models, fields, api


class pelicula(models.Model):
    _name = 'filmotecayubo.pelicula'
    _description = 'filmotecayubo.pelicula'


    code = fields.Char(string="Código", compute = "_get_code")
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
  
    genero_id=fields.Many2one("filmotecayubo.genero", string="Género", required=True, ondelete="cascade")
    tecnicas_id= fields.Many2many(comodel_name ="filmotecayubo.tecnica",
                                  relation = "tecnica_peliculas",
                                  columna1 = "pelicula_id",
                                  columna2 = "tecnica_id",
                                  string = "Técnicas")
    
    def _get_code(self):
          for pelicula in self:
               if len(pelicula.genero_id) == 0:
                    pelicula.code = "FILM_"+str(pelicula.id)
               else:
                    pelicula.code = str(pelicula.genero_id.name).upper()+ "_"+str(pelicula.id)
    
    def toggle_color(self):
         self.is_spanish = not self.is_spanish


    def f_create(self):
               pelicula = {
               "name": "Prueba ORM",
               "color": "cl",
               "genero_id": 2,
               "start_date": str(datetime.date(2022,8,8))
               } 
               print(pelicula)
               self.env['filmotecayubo.pelicula'].create(pelicula)
     
    def f_search_update(self):
          pelicula = self.env['filmotecayubo.pelicula'].search([('name', '=', 'asdas')])
          print('search()', pelicula, pelicula.name)