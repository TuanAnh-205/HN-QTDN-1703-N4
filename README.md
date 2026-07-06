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

## 🚀 3. Các chức năng chính

Module Enterprise Project Management được xây dựng nhằm hỗ trợ doanh nghiệp quản lý dự án và công việc trên nền tảng Odoo 15. Các chức năng chính của module bao gồm:

Quản lý dự án: Cho phép tạo mới, chỉnh sửa, cập nhật và quản lý thông tin dự án như mã dự án, tên dự án, trưởng dự án, thành viên tham gia, thời gian bắt đầu, thời gian kết thúc và trạng thái dự án.
Quản lý công việc: Hỗ trợ tạo, chỉnh sửa và theo dõi các công việc thuộc từng dự án, bao gồm thông tin về mã công việc, tên công việc, người phụ trách, mức độ ưu tiên, thời hạn hoàn thành và tiến độ thực hiện.
Phân công nhân viên: Tích hợp với module Quản lý Nhân sự (HRM) của Odoo, cho phép lựa chọn và phân công nhân viên phụ trách từng công việc trong dự án.
Tự động sinh công việc: Khi dự án được xác nhận, hệ thống tự động tạo các công việc mặc định và phân công cho các thành viên tham gia dự án, giúp giảm thời gian thao tác và chuẩn hóa quy trình quản lý.
Theo dõi tiến độ: Cho phép cập nhật tiến độ thực hiện của từng công việc theo tỷ lệ phần trăm, đồng thời hiển thị tiến độ tổng thể của dự án thông qua thanh tiến trình.
Tự động cập nhật trạng thái: Hệ thống tự động thay đổi trạng thái của công việc và dự án dựa trên tiến độ thực hiện, giúp người quản lý dễ dàng theo dõi tình hình triển khai.
Quản lý quyền truy cập: Phân quyền người dùng theo các nhóm như Project Administrator, Project Manager và Project Employee, đảm bảo mỗi người dùng chỉ được phép thực hiện các chức năng phù hợp với vai trò của mình.
Giao diện trực quan: Xây dựng giao diện quản lý bằng XML trên nền tảng Odoo với các danh sách, biểu mẫu và menu chức năng rõ ràng, giúp người dùng thao tác thuận tiện và dễ sử dụng.
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

    
