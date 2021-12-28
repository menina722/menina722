# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Presence',
    'version': '1.0',
    'category': 'hr',
    'description': "Just for testing",
    'depends': ['hr_attendance'],
    'data': [
            'security/ir.model.access.csv',
            'views/pr.xml',
             ],
    'website': 'https://www.odoo.com/app/employees',
}
