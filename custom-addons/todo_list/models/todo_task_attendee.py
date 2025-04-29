# -*- coding: utf-8 -*-
from odoo import models, fields

class TodoTaskAttendee(models.Model):
    """ Represents an attendee linked to a specific task. """
    _name = 'todo.task.attendee'
    _description = 'Task Attendee'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)

    task_id = fields.Many2one(
        'todo.task',
        string='Task',
        required=True,
        ondelete='cascade'
    )

    partner_id = fields.Many2one(
        'res.users',
        string='Attendee',
        required=True,
        ondelete='restrict'
    )