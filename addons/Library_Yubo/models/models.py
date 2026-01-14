# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

# 1. Herencia del modelo: hereda del modelo existente de lector / partner 
class Member(models.Model):
    _inherit = 'res.partner'  
    
    member_number = fields.Char(string='Número de Socio')

# 2. Modelo de Autor
class Author(models.Model):
    _name = 'library_yubo.author'
    _description = 'Autores de libros'

    name = fields.Char(string='Nombre', required=True)
    # Relación One2many: un autor puede tener varios libros 
    book_ids = fields.One2many('library_yubo.book', 'author_id', string='Libros')


    total_loans = fields.Integer(string="Total Préstamos", compute="_get_total_loans")

    def _get_total_loans(self):
        # Utilice env para obtener el modelo de préstamo
        Loan = self.env['library_yubo.loan']
        for author in self:
            # Busque todos los libros de este autor
            # Cuente cuántas veces se han tomado prestados estos libros
            count = Loan.search_count([('book_id.author_id', '=', author.id)])
            author.total_loans = count

# 3. Modelo de Libro (versión actualizada)
class Book(models.Model):
    _name = 'library_yubo.book'
    _description = 'Libros de la biblioteca'

    name = fields.Char(string='Título', required=True)
    # Relación Many2one: varios libros corresponden a un autor 
    author_id = fields.Many2one('library_yubo.author', string='Autor')
    # Relación Many2many: un libro puede pertenecer a varios géneros 
    genre_ids = fields.Many2many('library_yubo.genre', string='Géneros')
    
    state = fields.Selection([
        ('available', 'Disponible'), 
        ('borrowed', 'Prestado')
    ], string='Estado', default='available')

# 4. Modelo de Género de Libro
class Genre(models.Model):
    _name = 'library_yubo.genre'
    _description = 'Géneros de libros'
    
    name = fields.Char(string='Género', required=True)

# 5. Modelo de Préstamo 
class Loan(models.Model):
    _name = 'library_yubo.loan'
    _description = 'Registro de préstamos'

    book_id = fields.Many2one('library_yubo.book', string='Libro', required=True)
    member_id = fields.Many2one('res.partner', string='Socio', required=True)
    

    author_id = fields.Many2one(
        'library_yubo.author',
        string="Autor",
        related='book_id.author_id', # Encuentra author_id usando book_id
        readonly=True,
        store=True
    )

    # Uso de lambda para establecer el valor por defecto 
    loan_date = fields.Date(
        string='Fecha de Préstamo',
        default=lambda self: fields.Date.today()
    )
    return_date = fields.Date(string='Fecha de Devolución')
    
    # Campo calculado avanzado (almacenado en la base de datos) 
    duration = fields.Integer(
        string='Días de Préstamo',
        compute='_compute_duration',
        store=True  # <--- Significa que se almacena en una base de datos.
    )

    # Decorador @api.depends 
    @api.depends('loan_date', 'return_date')
    def _compute_duration(self):
        for record in self:
            if record.loan_date and record.return_date:
                record.duration = (record.return_date - record.loan_date).days
            else:
                record.duration = 0

    # Decorador @api.constrains (manejo de errores) 
    @api.constrains('return_date')
    def _check_return_date(self):
        for record in self:
            if record.return_date and record.return_date < record.loan_date:
                raise ValidationError(
                    'La fecha de devolución no puede ser anterior a la de préstamo.'
                )
    name = fields.Char(string="Referencia Préstamo", compute="_get_loan_ref", store=True)

    @api.depends('book_id', 'member_id')
    def _get_loan_ref(self):
        for loan in self:
            if loan.book_id and loan.member_id:
                # genera id 
                loan.name = f"{loan.book_id.name[:3].upper()}_{loan.member_id.name[:3].upper()}_{loan.id}"
            else:
                loan.name = "NEW"

   