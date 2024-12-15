import tkinter as tk

import random
import string

from tkinter import messagebox
from user import login, insertUser, checkExistEmail, getUserList, updateUserPassword

def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


# Hàm băm mật khẩu (sử dụng đơn giản ở đây, nhưng nên dùng thư viện như bcrypt trong thực tế)
def hash_password(password):
    return password  # Chỉ là mã giả, bạn nên băm mật khẩu trong thực tế

# Hàm kiểm tra email hợp lệ
def is_valid_email(email):
    return "@" in email and "." in email

# Chuyển hướng từ trang đăng ký về trang đăng nhập
def switch_to_login():
    frame_register.pack_forget()
    frame_login.pack()

# Mở giao diện Admin Panel
def open_admin_panel():
    admin_panel = tk.Toplevel(root)
    admin_panel.title("Admin Panel")
    admin_panel.config(bg="#92B9E3")
    tk.Label(admin_panel, text="Admin Panel", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)

    # Quản lý người dùng
    def create_user():
        # Tạo người dùng mới
        pass

    def edit_user():
        # Chỉnh sửa thông tin người dùng
        pass

    def delete_user():
        # Xóa tài khoản người dùng
        pass
    
    user_list = tk.Listbox(admin_panel, width=50)
    user_list.pack(pady=10)

    userDatabase = getUserList()
    
    for user in userDatabase:
        user_list.insert(tk.END, f"{user['full_name']} ({user['email']}) - Vai trò: {user['role']}")
  
    tk.Button(admin_panel, text="Tạo người dùng mới", command=create_user, bg="#FFC4A4", fg="#C688EB").pack(pady=5)
    tk.Button(admin_panel, text="Chỉnh sửa người dùng", command=edit_user, bg="#FFC4A4", fg="#C688EB").pack(pady=5)
    tk.Button(admin_panel, text="Xóa người dùng", command=delete_user, bg="#FFC4A4", fg="#C688EB").pack(pady=5)
    tk.Button(admin_panel, text="Thoát", command=admin_panel.destroy, bg="#FFC4A4", fg="#C688EB").pack()
    
    
# Mở giao diện Manager Dashboard
def open_manager_dashboard():
    manager_dashboard = tk.Toplevel(root)
    manager_dashboard.title("Manager Dashboard")
    manager_dashboard.config(bg="#92B9E3")
    tk.Label(manager_dashboard, text="Manager Dashboard", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
    
    def send_notification():
        # Gửi thông báo khuyến mãi
        pass

    tk.Button(manager_dashboard, text="Gửi thông báo khuyến mãi", command=send_notification, bg="#FFC4A4", fg="#C688EB").pack(pady=10)

    tk.Button(manager_dashboard, text="Thoát", command=manager_dashboard.destroy, bg="#FFC4A4", fg="#C688EB").pack()

# Mở giao diện Staff Dashboard
def open_staff_dashboard():
    staff_dashboard = tk.Toplevel(root)
    staff_dashboard.title("Staff Dashboard")
    staff_dashboard.config(bg="#92B9E3")
    tk.Label(staff_dashboard, text="Staff Dashboard", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
    
    def reset_password():
        # Reset mật khẩu
        pass

    tk.Button(staff_dashboard, text="Reset mật khẩu", command=reset_password, bg="#FFC4A4", fg="#C688EB").pack(pady=10)
    tk.Button(staff_dashboard, text="Thoát", command=staff_dashboard.destroy, bg="#FFC4A4", fg="#C688EB").pack()

# Mở giao diện Customer Dashboard
def open_customer_dashboard():
    customer_dashboard = tk.Toplevel(root)
    customer_dashboard.title("Customer Dashboard")
    customer_dashboard.config(bg="#92B9E3")
    tk.Label(customer_dashboard, text="Customer Dashboard", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
    
    def edit_info():
        # Chỉnh sửa thông tin cá nhân
        pass

    tk.Button(customer_dashboard, text="Chỉnh sửa thông tin", command=edit_info, bg="#FFC4A4", fg="#C688EB").pack(pady=10)
    tk.Button(customer_dashboard, text="Thoát", command=customer_dashboard.destroy, bg="#FFC4A4", fg="#C688EB").pack()

# Mở giao diện Quên Mật Khẩu
def open_forgot_password():
    frame_login.pack_forget()
    frame_forgot_password.pack()

# Đăng ký người dùng mới
def register_user():
    full_name = entry_full_name.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get().strip()
    confirm_password = entry_confirm_password.get().strip()
    role = role_var.get()  # Lấy vai trò người dùng
    
    if not full_name or not email or not password or not confirm_password or not role:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin vào tất cả các trường!")
        return
    
    if not is_valid_email(email):
        messagebox.showerror("Lỗi", "Email không hợp lệ! Vui lòng nhập đúng định dạng email.")
        return
    
    isValidEmail = checkExistEmail(email)
    
    if isValidEmail is not None:
        messagebox.showerror("Lỗi", "Email đã được đăng ký!")
        return
    
    if password != confirm_password:
        messagebox.showerror("Lỗi", "Mật khẩu không khớp!")
        return
    
    insertUser(email, password, role, full_name)

    messagebox.showinfo("Thành công", "Đăng ký thành công!")
    switch_to_login()

# Đăng nhập người dùng
def login_user():
    email = entry_login_email.get().strip()
    password = entry_login_password.get().strip()
    
    if not email or not password:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin vào tất cả các trường!")
        return

    validUser = login(email, password)
    if validUser is None:
        messagebox.showerror("Lỗi", "Email hoặc mật khẩu không đúng!")
        return
    role = validUser["role"]
    messagebox.showinfo("Thành công", f"Đăng nhập thành công! Vai trò: {role}")
    if role == "admin":
        open_admin_panel()
    elif role == "manager":
        open_manager_dashboard()
    elif role == "staff":
        open_staff_dashboard()
    elif role == "customer":
        open_customer_dashboard()
        
# Khôi phục mật khẩu
def reset_password():
    email = entry_forgot_email.get().strip()

    if not email:
        messagebox.showerror("Lỗi", "Vui lòng nhập email!")
        return

    if not is_valid_email(email):
        messagebox.showerror("Lỗi", "Email không hợp lệ!")
        return

    user = checkExistEmail(email)
    if user is None:
        messagebox.showerror("Lỗi", "Email không tồn tại trong hệ thống!")
        return

    # Mật khẩu mới (có thể thay bằng thư viện random)
    new_password = generate_random_password()
    updateUserPassword(email, new_password)
    messagebox.showinfo("Thành công", f"Mật khẩu mới của bạn là: {new_password}")
    switch_to_login()


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý người dùng")
root.config(bg="#92B9E3")

# Frame đăng nhập
frame_login = tk.Frame(root, bg="#92B9E3")
frame_login.pack(padx=10, pady=10)

tk.Label(frame_login, text="Đăng nhập", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
tk.Label(frame_login, text="Email:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_login_email = tk.Entry(frame_login, bg="#F1F1F1", fg="#6C7EE1")
entry_login_email.pack(fill="x", padx=10, pady=5)

tk.Label(frame_login, text="Mật khẩu:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_login_password = tk.Entry(frame_login, show="*", bg="#F1F1F1", fg="#6C7EE1")
entry_login_password.pack(fill="x", padx=10, pady=5)

tk.Button(frame_login, text="Đăng nhập", command=login_user, bg="#FFC4A4", fg="#C688EB").pack(pady=10)
tk.Button(frame_login, text="Quên mật khẩu?", command=open_forgot_password, bg="#FFC4A4", fg="#C688EB").pack(pady=5)

tk.Label(frame_login, text="Chưa có tài khoản? ", bg="#92B9E3", fg="#6C7EE1").pack(side="left", padx=10)
tk.Button(frame_login, text="Đăng ký", command=lambda: frame_login.pack_forget() or frame_register.pack(), bg="#FFC4A4", fg="#C688EB").pack(side="left", padx=5)

# Frame đăng ký
frame_register = tk.Frame(root, bg="#92B9E3")
frame_register.pack_forget()  # Ẩn ban đầu

tk.Label(frame_register, text="Đăng ký", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
tk.Label(frame_register, text="Họ tên:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_full_name = tk.Entry(frame_register, bg="#F1F1F1", fg="#6C7EE1")
entry_full_name.pack(fill="x", padx=10, pady=5)

tk.Label(frame_register, text="Email:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_email = tk.Entry(frame_register, bg="#F1F1F1", fg="#6C7EE1")
entry_email.pack(fill="x", padx=10, pady=5)

tk.Label(frame_register, text="Mật khẩu:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_password = tk.Entry(frame_register, show="*", bg="#F1F1F1", fg="#6C7EE1")
entry_password.pack(fill="x", padx=10, pady=5)

tk.Label(frame_register, text="Nhập lại mật khẩu:", bg="#92B9E3", fg="#6C7EE1").pack(anchor="w", padx=10)
entry_confirm_password = tk.Entry(frame_register, show="*", bg="#F1F1F1", fg="#6C7EE1")
entry_confirm_password.pack(fill="x", padx=10, pady=5)

# Frame Quên Mật Khẩu
frame_forgot_password = tk.Frame(root, bg="#92B9E3")
frame_forgot_password.pack_forget()

tk.Label(frame_forgot_password, text="Quên Mật Khẩu", font=("Arial", 16), bg="#92B9E3", fg="#6C7EE1").pack(pady=10)
entry_forgot_email = tk.Entry(frame_forgot_password, bg="#F1F1F1", fg="#6C7EE1")
entry_forgot_email.pack(fill="x", padx=10, pady=5)
tk.Button(frame_forgot_password, text="Khôi phục mật khẩu", command=reset_password, bg="#FFC4A4", fg="#C688EB").pack(pady=10)
tk.Button(frame_forgot_password, text="Quay lại Đăng Nhập", command=switch_to_login, bg="#FFC4A4", fg="#C688EB").pack()

# Chọn vai trò
role_var = tk.StringVar(value="customer")
tk.Label(frame_register, text="Vai trò:", bg="#92B9E3").pack(anchor="w", padx=10)
tk.Radiobutton(frame_register, text="Admin", variable=role_var, value="admin", bg="#92B9E3").pack(anchor="w", padx=10)
tk.Radiobutton(frame_register, text="Manager", variable=role_var, value="manager", bg="#92B9E3").pack(anchor="w", padx=10)
tk.Radiobutton(frame_register, text="Staff", variable=role_var, value="staff", bg="#92B9E3").pack(anchor="w", padx=10)
tk.Radiobutton(frame_register, text="Customer", variable=role_var, value="customer", bg="#92B9E3").pack(anchor="w", padx=10)

tk.Button(frame_register, text="Đăng ký", command=register_user, bg="#FFC4A4", fg="#C688EB").pack(pady=10)

# Liên kết trở lại màn hình đăng nhập
tk.Label(frame_register, text="Đã có tài khoản?", bg="#92B9E3", fg="#6C7EE1").pack(side="left", padx=10)
tk.Button(frame_register, text="Đăng nhập", command=switch_to_login, bg="#FFC4A4", fg="#C688EB").pack(side="left", padx=5)


# Chạy ứng dụng
root.mainloop()
