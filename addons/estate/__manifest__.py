{
    'name': 'Estate',
    'version': '1.0.0',
    'summary': 'Housing Management',
    'description': "",
    'website': 'https://www.odoo.com/page/estate',
    'depends': [
        'base_setup',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}