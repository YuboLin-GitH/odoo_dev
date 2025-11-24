# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class task(models.Model):
    _name = 'manageyubo.task'
    _description = 'manageyubo.task'

    name = fields.Char(string="Nombre")
    description = fields.Char()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()

    history_id=fields.Many2one("manageyubo.history", string="Historia", required=True, ondelete="cascade")

    sprint_id=fields.Many2one("manageyubo.sprint", string="Sprint", required=True, ondelete="cascade")

    technology_id = fields.Many2many(
        comodel_name="manageyubo.technology",
        relation="technology_task",
        column1="task_id",
        column2="technology_id",  
        string = "Tecnologia")

class project(models.Model):
    _name = 'manageyubo.project'
    _description = 'manageyubo.project'

    name = fields.Char()
    description = fields.Char()
    
    history_id=fields.One2many("manageyubo.history", inverse_name="project_id", string="Historia")

    sprint_id=fields.One2many("manageyubo.sprint", inverse_name="project_id", string="Sprints")

class sprint(models.Model):
    _name = 'manageyubo.sprint'
    _description = 'manageyubo.sprint'

    name = fields.Char()
    description = fields.Char()

    duration = fields.Integer()

    start_date = fields.Datetime()
    end_date = fields.Datetime(compute="_get_end_date", store=True)

    project_id=fields.Many2one("manageyubo.project", string="Proyecto", required=True, ondelete="cascade")

    task_id=fields.One2many("manageyubo.task", inverse_name="sprint_id", string="Tareas")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            #try:
                if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                    sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
                else:
                    sprint.end_date = sprint.start_date

class history(models.Model):
    _name = 'manageyubo.history'
    _description = 'manageyubo.history'

    name = fields.Char()
    description = fields.Char()

    project_id=fields.Many2one("manageyubo.project", string="Proyecto", required=True, ondelete="cascade")

    task_id=fields.One2many("manageyubo.task", inverse_name="history_id", string="Tareas")

   
class technology(models.Model):
    _name = 'manageyubo.technology'
    _description = 'manageyubo.technology'

    name = fields.Char()
    description = fields.Char()
    photo = fields.Image()

    task_id = fields.Many2many(
        comodel_name="manageyubo.task",
        relation="technology_task",
        column1="technology_id",
        column2="task_id",
        string = "Tareas")
    


   