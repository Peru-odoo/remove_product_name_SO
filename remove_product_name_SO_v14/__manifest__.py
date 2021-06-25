# -*- coding: utf-8 -*-
{
    'name': "Remove Product Name SO",
    'version': '1.2',
    'license': 'OPL-1',
    'category': 'Sales Management',
    'summary': 'Remove Product Name SO allows you to remove the product name automatically added in the product '
               'description. Ideal, to avoid having to delete the product name each time.',
    'description': """
        -------------------------------------------------------------------------
        Allows you to remove the product name automatically added in the product description.
        -------------------------------------------------------------------------
    """,
    'author': "Omydoo",
    'website': "https://www.omydoo.fr",
    'maintainer': 'Omydoo',
    'depends': ['base', 'sale_management'],
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'active': False,
    'images': ['static/description/invoiced-ref-client-odoo-cover.gif'],
    'support': 'support@omydoo.fr',
    'price': 9.99,
    'currency': 'EUR',
}
