# __manifest__.py
{
    'name': 'Modul Pemesanan Ruangan',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Modul untuk mengelola pemesanan ruangan',
    'author': 'Firmansyah Surwa Adi Laksono',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/master_ruangan_views.xml',
        'views/pemesanan_ruangan_views.xml',
    ],
    'installable': True,
    'application': True,
}
