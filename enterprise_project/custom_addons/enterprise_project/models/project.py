from odoo import models, fields, api
from datetime import timedelta


class EnterpriseProject(models.Model):
    _name = 'enterprise.project'
    _description = 'Quản lý dự án'
    _order = 'id desc'

    code = fields.Char(
        string='Mã dự án',
        readonly=True,
        copy=False,
        default='New'
    )

    name = fields.Char(
        string='Tên dự án',
        required=True
    )

    manager_id = fields.Many2one(
        'hr.employee',
        string='Trưởng dự án'
    )

    member_ids = fields.Many2many(
        'hr.employee',
        string='Thành viên dự án'
    )

    start_date = fields.Date(
        string='Ngày bắt đầu'
    )

    end_date = fields.Date(
        string='Ngày kết thúc'
    )

    state = fields.Selection([
        ('new', 'Mới'),
        ('doing', 'Đang thực hiện'),
        ('done', 'Hoàn thành')
    ],
        string='Trạng thái',
        default='new'
    )

    task_ids = fields.One2many(
        'enterprise.task',
        'project_id',
        string='Danh sách công việc'
    )

    task_count = fields.Integer(
        string='Tổng công việc',
        compute='_compute_statistics'
    )

    completed_task = fields.Integer(
        string='Đã hoàn thành',
        compute='_compute_statistics'
    )

    progress = fields.Float(
        string='Tiến độ (%)',
        compute='_compute_statistics',
        store=True
    )

    @api.depends('task_ids.state')
    def _compute_statistics(self):
        for project in self:
            total = len(project.task_ids)
            done = len(project.task_ids.filtered(lambda x: x.state == 'done'))

            project.task_count = total
            project.completed_task = done

            if total:
                project.progress = done * 100 / total
            else:
                project.progress = 0

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'enterprise.project'
            ) or 'New'

        return super().create(vals)

    def action_confirm(self):
        """
        Khi xác nhận dự án:
        - Tự tạo 3 công việc mặc định
        - Tự gán nhân viên
        - Tự tính deadline
        """

        for project in self:

            if project.state != 'new':
                continue

            if not project.member_ids:
                continue

            tasks = [
                "Khảo sát yêu cầu",
                "Thiết kế hệ thống",
                "Lập trình"
            ]

            members = project.member_ids

            for index, task_name in enumerate(tasks):

                employee = members[index % len(members)]

                deadline = project.start_date

                if project.start_date:
                    deadline = project.start_date + timedelta(days=(index + 1) * 3)

                self.env['enterprise.task'].create({
                    'name': task_name,
                    'project_id': project.id,
                    'employee_id': employee.id,
                    'start_date': project.start_date,
                    'deadline': deadline,
                    'priority': '1',
                    'progress': 0,
                    'description': task_name,
                })

            project.state = 'doing'
