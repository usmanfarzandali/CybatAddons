# -*- coding: utf-8 -*-
# Part of Cybat. See LICENSE file for full copyright and licensing details.

{
    "name" : "HR Employee Age",
    "version" : "14.0.0.0",
    "category" : "Employee",
    'summary': "This odoo app helps to show employee age, On entering employee date of birth, employee age will automatically displayed.",
    "description": """
    
        This odoo app helps to show employee age, On entering employee date of birth, employee age will automatically displayed.
    
    """,
    "author": "Usman Farzand",
    "website" : "https://www.cybat.net",
    "price": 0.00,
    "currency": 'EUR',
    "depends" : ['hr'],
    "data": [
        'views/hr_inherit_views.xml',   
    ],
    "qweb" : [],
    "auto_install": False,
    "installable": True,
    "images":["static/description/Banner.png"],
}
