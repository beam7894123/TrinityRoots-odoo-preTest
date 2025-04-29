# -*- coding: utf-8 -*-
{
    'name': 'ToDoList',
    'version': '1.0',
    'summary': 'ToDo List',
    'sequence': 10,
    'description': """
ToDo List
====================
""",
    'category': 'ToDoList/ToDoList',
    'website': 'https://www.bezathecat.com',
    'author': 'Bezathecat',
    'depends': [
        'base',
        ],
    'data': [
        'security/ir.model.access.csv',
        
        'data/todo_task_tag_data.xml',
        
        'views/todo_task_views.xml',
        'views/todo_menus.xml',
        ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
