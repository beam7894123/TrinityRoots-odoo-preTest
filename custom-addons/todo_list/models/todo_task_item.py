# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTaskItem(models.Model):
    _name = 'todo.task.item'
    _description = 'To-Do Task Checklist Item'
    _order = 'sequence, id'

    task_id = fields.Many2one(
        'todo.task',
        string='Task',
        required=True,
        ondelete='cascade',
        index=True
    )
    sequence = fields.Integer(string='Sequence', default=10)
    title = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Is Complete', default=False)