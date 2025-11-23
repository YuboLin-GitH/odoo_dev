# -*- coding: utf-8 -*-
# from odoo import http


# class Manageyubo(http.Controller):
#     @http.route('/manageyubo/manageyubo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageyubo/manageyubo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageyubo.listing', {
#             'root': '/manageyubo/manageyubo',
#             'objects': http.request.env['manageyubo.manageyubo'].search([]),
#         })

#     @http.route('/manageyubo/manageyubo/objects/<model("manageyubo.manageyubo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageyubo.object', {
#             'object': obj
#         })

