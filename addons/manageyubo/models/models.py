# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class task(models.Model):
    _name = 'manageyubo.task'
    _description = 'manageyubo.task'

    code = fields.Char(string="Código", compute = "_get_code", store=True)
    name = fields.Char(string="Nombre")
    description = fields.Char()
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    is_paused = fields.Boolean()

    history_id=fields.Many2one("manageyubo.history", string="Historia", required=True, ondelete="cascade")

    sprint_id=fields.Many2one("manageyubo.sprint",compute= "_get_sprint", string="Sprint", store=True)

    technology_id = fields.Many2many(
        comodel_name="manageyubo.technology",
        relation="technology_task",
        column1="task_id",
        column2="technology_id",  
        string = "Tecnologia")
    
    project_id = fields.Many2one(
    'manageyubo.project',
    string="Proyecto",
    related='history_id.project_id',
    readonly=True
    )
    
    definition_date = fields.Datetime(default=lambda p: datetime.datetime.now())


    @api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['manageyubo.sprint'].search([('project_id', '=', task.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
                    break
            if not found:
                task.sprint_id = False
    
    @api.depends('history_id')
    def _get_code(self):
        for task in self:
            if not task.history_id:
                task.code = "TSK_" + str(task.id)
            else:
                task.code = str(task.history_id.name).upper() + "_" + str(task.id)

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

    duration = fields.Integer(default=15)

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

    used_technologies = fields.Many2many("manageyubo.technology", compute="_get_used_technologies")

    def _get_used_technologies(self):
        Technology = self.env['manageyubo.technology']
        for history in self:
            technologies = Technology
            for task in history.task_id:
                if not technologies:
                    technologies = task.technology_id
                else:
                    technologies = technologies + task.technology_id
            history.used_technologies = technologies
   
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
    


   