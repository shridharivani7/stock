# -*- coding: utf-8 -*-

###################################################################################
#
#
#
###################################################################################

{
    'name': 'Stock Extended',
    'version': '12.0.1.0.1',
    'summary': 'Extra Fields',
    'author': 'Shridhar IVani',
    'maintainer': 'Public',
    'company': '',
    'website': '',
    'depends': ['stock','base'],
    'category': 'Inventory',
    'demo': [],
    'data': ['views/stock_picking.xml',
            'reports/report_deliveryslip_extended.xml',
            'reports/stock_report_views.xml',],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
    'qweb': [],
    'license': 'AGPL-3',
}
