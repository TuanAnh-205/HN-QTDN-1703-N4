<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<h2 align="center">
    PLATFORM ERP
</h2>
<div align="center">
    <p align="center">
        <img src="docs/logo/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/logo/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/logo/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

## 📖 1. Giới thiệu
Dự án Enterprise Project Management được xây dựng trên nền tảng Odoo 15 nhằm hỗ trợ doanh nghiệp quản lý dự án và công việc một cách hiệu quả. Module cho phép người dùng tạo và quản lý dự án, phân công công việc cho nhân viên, theo dõi tiến độ thực hiện, tự động cập nhật trạng thái công việc và dự án, đồng thời tích hợp với module Quản lý Nhân sự (HRM) của Odoo để quản lý thông tin nhân viên. Với giao diện trực quan, dễ sử dụng và khả năng tự động hóa một số nghiệp vụ, module góp phần nâng cao hiệu quả quản lý, giảm thời gian xử lý công việc và đáp ứng nhu cầu quản lý dự án trong doanh nghiệp.

## 🔧 2. Các công nghệ được sử dụng
<div align="center">

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>

## 🚀 3# 🚀 Enterprise Project Management (Odoo 15)

## 📌 Giới thiệu

**Enterprise Project Management** là module được phát triển trên nền tảng **Odoo 15**, hỗ trợ doanh nghiệp quản lý dự án, quản lý công việc và phân công nhân sự một cách hiệu quả. Module giúp theo dõi tiến độ thực hiện dự án, tự động hóa một số quy trình quản lý và tích hợp trực tiếp với module **Human Resources (HR)** của Odoo.

---

# ✨ Các chức năng chính

## 📁 1. Quản lý Dự án

- Tạo, chỉnh sửa và xóa dự án.
- Tự động sinh mã dự án.
- Quản lý trưởng dự án và thành viên tham gia.
- Theo dõi thời gian bắt đầu và kết thúc.
- Theo dõi trạng thái dự án.
- Thống kê số lượng công việc.
- Hiển thị tiến độ dự án bằng Progress Bar.

---

## ✅ 2. Quản lý Công việc

- Tạo và quản lý công việc.
- Tự động sinh mã công việc.
- Phân công nhân viên phụ trách.
- Thiết lập ngày bắt đầu và hạn hoàn thành.
- Cập nhật tiến độ thực hiện.
- Quản lý mức độ ưu tiên.
- Theo dõi trạng thái công việc.

---

## 👨‍💼 3. Quản lý Nhân sự

- Tích hợp với module HR của Odoo.
- Lựa chọn trưởng dự án.
- Quản lý thành viên dự án.
- Phân công công việc cho nhân viên.
- Liên kết dữ liệu giữa Dự án và Nhân sự.

---

## ⚙️ 4. Tự động hóa

- Tự động sinh công việc khi xác nhận dự án.
- Tự động cập nhật trạng thái công việc.
- Tự động cập nhật tiến độ dự án.
- Tự động chuyển trạng thái dự án khi hoàn thành.

---

## 🔐 5. Phân quyền

- Project Administrator
- Project Manager
- Project Employee

Hệ thống phân quyền theo từng nhóm người dùng nhằm đảm bảo tính bảo mật và kiểm soát dữ liệu.

---

## 🖥️ Giao diện

- Danh sách dự án
- Form quản lý dự án
- Danh sách công việc
- Form quản lý công việc
- Progress Bar theo dõi tiến độ
- Menu quản lý trực quan

---

# 📂 Cấu trúc Module

```text
enterprise_project
├── __init__.py
├── __manifest__.py
├── models
│   ├── __init__.py
│   ├── project.py
│   └── task.py
├── views
│   ├── project_views.xml
│   └── task_views.xml
├── security
│   ├── security.xml
│   └── ir.model.access.csv
└── data
    └── sequence.xml
```

---

# 🛠️ Công nghệ sử dụng

- Odoo 15 Community
- Python 3
- XML
- PostgreSQL
- Ubuntu Linux
- Visual Studio Code

---

# 👨‍🎓 Thông tin

**Đề tài:** Enterprise Project Management

**Nền tảng:** Odoo 15 ERP

**Ngôn ngữ:** Python + XML

**Cơ sở dữ liệu:** PostgreSQL
## ⚙️ 4. Cài đặt

### 4.1. Cài đặt công cụ, môi trường và các thư viện cần thiết

#### 4.1.1. Tải project.
```
git clone https://github.com/FIT-DNU/Business-Internship.git
```
#### 4.1.2. Cài đặt các thư viện cần thiết
Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
#### 4.1.3. Khởi tạo môi trường ảo.
- Khởi tạo môi trường ảo
```
python3.10 -m venv ./venv
```
- Thay đổi trình thông dịch sang môi trường ảo
```
source venv/bin/activate
```
- Chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu
```
pip3 install -r requirements.txt
```
### 4.2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.
```
sudo docker-compose up -d
```
### 4.3. Setup tham số chạy cho hệ thống
Tạo tệp **odoo.conf** có nội dung như sau:
```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5431
xmlrpc_port = 8069
```
Có thể kế thừa từ file **odoo.conf.template**
### 4.4. Chạy hệ thống và cài đặt các ứng dụng cần thiết
Lệnh chạy
```
python3 odoo-bin.py -c odoo.conf -u all
```
Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

## 📝 5. License

© 2024 AIoTLab, Faculty of Information Technology, DaiNam University. All rights reserved.

---

    
