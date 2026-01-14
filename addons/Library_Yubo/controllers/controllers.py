# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class LibraryYubo(http.Controller):

    # 1. API: Obtener la lista completa de libros (GET)
    # Dirección de acceso: http://localhost:8069/api/books
    @http.route('/api/books', auth='public', type='http', methods=['GET'], csrf=False)
    def get_books(self, **kw):
        books = request.env['library_yubo.book'].sudo().search([])
        book_list = []
        for book in books:
            book_list.append({
                'id': book.id,
                'title': book.name,
                'author': book.author_id.name,
                'state': book.state,
            })
        
        return request.make_response(
            json.dumps({'status': 200, 'data': book_list}),
            headers={'Content-Type': 'application/json'}
        )