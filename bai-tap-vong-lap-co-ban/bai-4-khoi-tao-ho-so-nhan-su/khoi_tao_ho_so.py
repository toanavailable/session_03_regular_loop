"""Kiosk Nhập liệu Nhân sự - Khởi tạo hồ sơ cho 3 nhân sự mới (TechCorp)."""

# ========== KHỞI TẠO ==========
new_employee_count = 3
line_width = 55
warning_message = "[CẢNH BÁO] Dữ liệu trống hoặc không hợp lệ. Hủy tạo hồ sơ cho nhân viên này."
created_count = 0   # đếm số hồ sơ tạo thành công

print("=" * line_width)
print(f"{'KIOSK NHẬP LIỆU NHÂN SỰ - TECHCORP':^{line_width}}")
print("=" * line_width)

# ========== VÒNG LẶP NHẬP LIỆU: đúng 3 lần cho 3 nhân viên ==========
for employee_number in range(1, new_employee_count + 1):
    print(f"\n>>> Nhân viên mới thứ {employee_number}/{new_employee_count}")

    # --- Nhập dữ liệu ---
    employee_id = input("Mã nhân viên (VD: NV001, DEV009): ")
    full_name = input("Họ và tên (VD: Nguyễn Văn An): ")
    department = input("Phòng ban công tác (VD: IT, Marketing, Kế toán): ")

    # --- Chuẩn hóa: chuỗi toàn dấu cách sẽ thành chuỗi rỗng "" ---
    employee_id = employee_id.strip().upper()
    full_name = " ".join(full_name.split()).title()
    department = " ".join(department.split())

    # --- Kiểm tra bẫy dữ liệu: trống hoặc chỉ có khoảng trắng ---
    if employee_id == "" or full_name == "":
        print(warning_message)
        continue   # KHÔNG in phiếu, chuyển ngay sang nhân viên tiếp theo

    if department == "":
        department = "Chưa phân bổ"

    # --- In Phiếu Hồ sơ Điện tử ---
    created_count += 1
    print("-" * line_width)
    print(f"{'PHIẾU HỒ SƠ ĐIỆN TỬ':^{line_width}}")
    print("-" * line_width)
    print(f"{'Mã nhân viên':<14}: {employee_id}")
    print(f"{'Họ và tên':<14}: {full_name}")
    print(f"{'Phòng ban':<14}: {department}")
    print("-" * line_width)

# ========== KẾT THÚC ==========
print("\n" + "=" * line_width)
print(f"Hoàn tất! Đã tạo {created_count}/{new_employee_count} hồ sơ nhân sự.")
print("=" * line_width)
