# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-Do Task'
    _order = 'start_datetime desc, id desc'

    # -- Fields --
    title = fields.Char(string='Title', required=True, tracking=True)
    tag_ids = fields.Many2many(
        'todo.task.tag',
        'todo_task_tag_rel',
        'task_id',
        'tag_id',
        string='Tags',
        tracking=True
    )
    start_datetime = fields.Datetime(
        string='Start Date',
        required=True,
        default=fields.Datetime.now,
        tracking=True
    )
    end_datetime = fields.Datetime(string='End Date', required=True, tracking=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Completed'),
        ], string='Status',
        default='draft',
        required=True,
        copy=False, # Don't copy status when duplicating record ;p
        tracking=True
    )
    attendee_ids = fields.One2many(
        comodel_name='todo.task.attendee',
        inverse_name='task_id',
        string='Attendees'
    )
    item_ids = fields.One2many(
        'todo.task.item',
        'task_id',
        string='Checklist Items'
    )

    all_items_done = fields.Boolean(
        string="All Items Done?",
        compute='_compute_all_items_done',
        store=False # No need to store, check on the fly
    )

    # -- Compute Methods --
    @api.depends('item_ids.is_done')
    def _compute_all_items_done(self):
        for task in self:
            if not task.item_ids:
                # If there are no items, consider it 'done' for the button logic
                task.all_items_done = True
            else:
                task.all_items_done = all(item.is_done for item in task.item_ids)

    # -- Action Methods (Buttons) --
    def action_start_progress(self):
        for task in self:
            if task.status == 'draft':
                task.status = 'in_progress'
            else:
                raise UserError(_("Task must be in Draft status to start progress."))
        return True

    def action_mark_complete(self):
        for task in self:
            if task.status != 'in_progress':
                raise UserError(_("Task must be In Progress to mark as Complete."))
            if not task.all_items_done:
                raise UserError(_("Not all checklist items are marked as done."))
            task.status = 'complete'
        return True

    # -- Constraints --
    @api.constrains('start_datetime', 'end_datetime')
    def _check_dates(self):
        for task in self:
            if task.start_datetime and task.end_datetime and task.start_datetime > task.end_datetime:
                raise UserError(_("End Date cannot be earlier than Start Date."))