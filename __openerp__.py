# -*- coding: utf-8 -*-
{
    'name': "Gila Purchase",

    'description': """
        This module will help to adapt purchase workflow
    """,

    'author': "Gila Desarrollos SA CV",
    'website': "http://www.gila.com.mx",
    'category': 'Purchase',
    'version': '9.0.0.1',

    'depends': ['base','purchase','project'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_view.xml',
    ],
}