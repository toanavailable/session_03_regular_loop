"""Kiosk HR Tự Phục Vụ - Cập nhật hồ sơ & Đánh giá năng lực (TechCorp)."""

# =====================================================================
# KHỐI 1: KHỞI TẠO
# =====================================================================
line_width = 60
min_kpi_score = 1.0
max_kpi_score = 5.0

print("=" * line_width)
print(f"{'KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI':^{line_width}}")
print("=" * line_width)

# Vòng lặp tổng: cho phép quản lý nhập liên tục nhiều nhân viên
while True:
    print("\n[Nhập thông tin nhân viên]")

    # =================================================================
    # KHỐI 2: THU THẬP DỮ LIỆU + KIỂM TRA (mỗi trường là một vòng lặp "bẫy chặn")
    # =================================================================
    # --- 1. Mã nhân viên (str, không rỗng) ---
    while True:
        employee_id = input("1. Enter Employee ID (VD: DEV01): ").strip().upper()
        if employee_id != "":
            break
        print("   [!] Lỗi: Mã nhân viên không được để trống. Vui lòng nhập lại!")

    # --- 2. Họ và tên (str, không rỗng) ---
    while True:
        employee_name = " ".join(input("2. Enter Full Name (VD: Nguyen Van A): ").split())
        if employee_name != "":
            break
        print("   [!] Lỗi: Họ và tên không được để trống. Vui lòng nhập lại!")

    # --- 3. Lương hiện tại (float > 0) ---
    while True:
        salary_text = input("3. Enter current Salary in VND (Number > 0, VD: 25000000): ").strip()
        # Bỏ dấu "-" ở đầu (nếu có) rồi kiểm tra phần còn lại có phải là số (cho phép 1 dấu chấm)
        unsigned_text = salary_text[1:] if salary_text.startswith("-") else salary_text
        if not unsigned_text.replace(".", "", 1).isdigit():
            print("   [!] Lỗi: Lương phải là một con số (VD: 25000000). Vui lòng nhập lại!")
            continue
        current_salary = float(salary_text)        # ép kiểu sau khi chắc chắn là số
        if current_salary <= 0:
            print("   [!] Lỗi: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
            continue
        break

    # --- 4. Điểm KPI (float, 1.0 - 5.0) ---
    while True:
        score_text = input("4. Enter Performance Score (1.0 to 5.0, VD: 4.5): ").strip()
        unsigned_text = score_text[1:] if score_text.startswith("-") else score_text
        if not unsigned_text.replace(".", "", 1).isdigit():
            print("   [!] Lỗi: Điểm KPI phải là một con số (VD: 4.5). Vui lòng nhập lại!")
            continue
        performance_score = float(score_text)
        if performance_score < min_kpi_score or performance_score > max_kpi_score:
            print(f"   [!] Lỗi: Điểm KPI phải nằm trong khoảng từ {min_kpi_score} đến {max_kpi_score}!")
            continue
        break

    # --- 5. Số năm kinh nghiệm (int >= 0) ---
    while True:
        experience_text = input("5. Enter Year of Experience (Integer >= 0, VD: 3): ").strip()
        if experience_text.isdigit():               # isdigit() đã chặn số âm, số lẻ, chữ
            experience_years = int(experience_text)
            break
        print("   [!] Lỗi: Số năm kinh nghiệm phải là số nguyên >= 0. Vui lòng nhập lại!")

    # =================================================================
    # KHỐI 3: HIỂN THỊ - HỒ SƠ ĐIỆN TỬ
    # =================================================================
    print("\n" + "=" * line_width)
    print(f"{'E-PROFILE CẬP NHẬT':^{line_width}}")
    print("=" * line_width)
    print(f"- ID         : {employee_id}")
    print(f"- Name       : {employee_name}")
    print(f"- Salary     : {current_salary:,.0f} VND")
    print(f"- KPI Score  : {performance_score} / {max_kpi_score}")
    print(f"- Experience : {experience_years} years")

    # =================================================================
    # KHỐI 4: HIỂN THỊ - LOG HỆ THỐNG (dành cho IT)
    # =================================================================
    print("\n" + "=" * line_width)
    print(f"{'IT SYSTEM LOG':^{line_width}}")
    print("=" * line_width)
    print(f"{'employee_id':<18} | {type(employee_id)}")
    print(f"{'employee_name':<18} | {type(employee_name)}")
    print(f"{'current_salary':<18} | {type(current_salary)}")
    print(f"{'performance_score':<18} | {type(performance_score)}")
    print(f"{'experience_years':<18} | {type(experience_years)}")
    print("=" * line_width)

    # =================================================================
    # KHỐI 5: HỎI TIẾP TỤC
    # =================================================================
    answer = input("\nDo you want to enter another employee? (y/n): ").strip().lower()
    while answer != "y" and answer != "n":
        answer = input("Vui lòng chỉ gõ 'y' hoặc 'n': ").strip().lower()

    if answer == "n":
        print("\nĐang tắt Kiosk... Tạm biệt!")
        break
