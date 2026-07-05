from odoo import models, fields, api


class EnterpriseTask(models.Model):
    _name = 'enterprise.task'
    _description = 'Quản lý công việc'
    _order = 'id desc'

    code = fields.Char(
        string='Mã công việc',
        readonly=True,
        copy=False,
        default='New'
    )

    name = fields.Char(
        string='Tên công việc',
        required=True
    )

    project_id = fields.Many2one(
        'enterprise.project',
        string='Dự án',
        required=True,
        ondelete='cascade'
    )

    employee_id = fields.Many2one(
        'hr.employee',
        string='Người phụ trách',
        required=True
    )

    start_date = fields.Date(
        string='Ngày bắt đầu'
    )

    deadline = fields.Date(
        string='Hạn hoàn thành'
    )

    priority = fields.Selection([
        ('0', 'Thấp'),
        ('1', 'Trung bình'),
        ('2', 'Cao')
    ],
        string='Ưu tiên',
        default='1'
    )

    progress = fields.Integer(
        string='Tiến độ (%)',
        default=0
    )

    description = fields.Text(
        string='Mô tả'
    )

    state = fields.Selection([
        ('new', 'Mới'),
        ('doing', 'Đang thực hiện'),
        ('done', 'Hoàn thành')
    ],
        string='Trạng thái',
        default='new'
    )

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'enterprise.task'
            ) or 'New'

        return super().create(vals)

    @api.onchange('progress')
    def _onchange_progress(self):
        if self.progress >= 100:
            self.state = 'done'
        elif self.progress > 0:
            self.state = 'doing'
        else:
            self.state = 'new'

    def write(self, vals):
        res = super().write(vals)

        for task in self:
            project = task.project_id

            if not project:
                continue

            total = len(project.task_ids)
            done = len(project.task_ids.filtered(lambda t: t.state == 'done'))

            if total == 0:
                project.state = 'draft'
            elif done == total:
                project.state = 'done'
            else:
                project.state = 'doing'

        return res
