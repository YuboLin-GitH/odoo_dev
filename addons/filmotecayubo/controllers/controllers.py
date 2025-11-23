# -*- coding: utf-8 -*-
# from odoo import http


# class Filmotecayubo(http.Controller):
#     @http.route('/filmotecayubo/filmotecayubo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filmotecayubo/filmotecayubo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('filmotecayubo.listing', {
#             'root': '/filmotecayubo/filmotecayubo',
#             'objects': http.request.env['filmotecayubo.filmotecayubo'].search([]),
#         })

#     @http.route('/filmotecayubo/filmotecayubo/objects/<model("filmotecayubo.filmotecayubo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filmotecayubo.object', {
#             'object': obj
#         })

