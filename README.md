# Lab-03--Testing-software-login-form-
## 1. Giới thiệu

Dự án **LAB03-LOGIN-FORM** là ví dụ về một form đăng nhập cơ bản, được kiểm thử bằng **Selenium (Python)**.  
Mục tiêu: mô phỏng quy trình đăng nhập và xác minh các luồng hoạt động của form.

**Các tính năng chính:**
- ✅ Đăng nhập thành công  
- ❌ Đăng nhập sai thông tin  
- ⚠️ Bỏ trống Username/Password  
- 🔗 Liên kết **Forgot password?**  
- 📝 Liên kết **SIGN UP**  
- 🌐 Nút đăng nhập qua mạng xã hội (**Facebook, Twitter, Google**)

---

## 2. Cấu trúc và mô tả thư mục

| 📁 **Tên file / thư mục** | 🧾 **Mô tả** |
|-----------------------------|--------------|
| `login.html` | Giao diện form đăng nhập (Username, Password, Login, Forgot password?, Sign Up, Social Login buttons) |
| `dashboard.html` | Trang hiển thị sau khi đăng nhập thành công |
| `forgot_password.py` | Xử lý khi người dùng chọn “Forgot password?” |
| `signup.py` | Xử lý đăng ký tài khoản mới |
| `social_buttons.py` | Logic đăng nhập thông qua mạng xã hội |
| `test_login_form.py` | File kiểm thử Selenium |
| `usecase_loginform.png` | Sơ đồ Use Case minh họa các tương tác của User |

---

## 3. Hướng dẫn cài đặt và chạy test

🔧Bước 1: Cài đặt môi trường

Yêu cầu **Python 3.x**  
Kiểm tra phiên bản:
python --version


🔧 Bước 2: Cài các thư viện cần thiết
Nếu dự án dùng Flask (chạy form web):

bash
Copy code
pip install flask
Cài Selenium:

bash
Copy code
pip install selenium
Cài WebDriver (ví dụ: ChromeDriver):

Tải tại: https:/chromedriver.chromium.org

Giải nén và đặt cùng thư mục với file test_login_form.py

🚀 Bước 3: Chạy ứng dụng (nếu có server)
Khởi động server web:

bash
Copy code
python login.py
Hoặc file chính bạn dùng để khởi chạy ứng dụng Flask.

🧠 Bước 4: Chạy script kiểm thử Selenium
Thực thi test:

bash
Copy code
python test_login_form.py
Khi chạy xong, hệ thống sẽ tự động mở trình duyệt, nhập dữ liệu test và hiển thị kết quả.

## 4 Tính năng & Luồng kiểm thử

| Tình huống | Dữ liệu nhập | Kết quả mong đợi |
|-------------|---------------|------------------|
| Đăng nhập đúng | Username & Password hợp lệ | Chuyển đến `dashboard.html` hoặc báo “Login success” |
| Sai thông tin đăng nhập | Username đúng, Password sai | Hiển thị “Invalid credentials” |
| Bỏ trống trường | Trống Username hoặc Password | Hiển thị “Please fill in username/password” |
| Forgot password? | Nhấn nút “Forgot password?” | Chuyển đến trang `forgot_password.py` |
| SIGN UP | Nhấn nút “Sign Up” | Chuyển sang `signup.py` |
| Social login | Nhấn các nút “Login with Facebook / Twitter / Google” | Hiển thị đủ 3 nút và có thể click được (mở popup đăng nhập tương ứng) |

## 5. Sơ đồ Use Case


![Sơ đồ Use Case](https://github.com/TranQuynh555/Lab-03--Testing-software-login-form-/blob/8d7430fc242732c7f9ab4d2976fd6858b00f7e71/usecase.png?raw=true)
