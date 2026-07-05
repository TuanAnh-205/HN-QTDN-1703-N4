{
    'name': 'Enterprise Project Management',
    'version': '15.0.1.0.0',

    'summary': 'Quản lý dự án + Quản lý công việc + HRM',

    'description': """
Enterprise Project Management

- Quản lý dự án
- Quản lý công việc
- Tích hợp HRM
- Tự động tạo công việc
- Theo dõi tiến độ
""",

    'author': 'Le Tuan Anh',
    'license': 'LGPL-3',

    'category': 'Project',

    'depends': [
        'base',
        'hr',
    ],

    'data': [

        'security/security.xml',
        'security/ir.model.access.csv',

        'data/sequence.xml',

        'views/project_views.xml',
        'views/task_views.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
