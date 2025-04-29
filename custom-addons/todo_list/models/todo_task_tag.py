# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TodoTaskTag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-Do Task Tag'
    _order = 'name'

    # --- Fields ---
    name = fields.Char(
        string='Tag Name',
        required=True
    )
    color = fields.Integer(
        string='Color Index'
    )

    # --- Constraints ---
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]