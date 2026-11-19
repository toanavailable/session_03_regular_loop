"""Chức năng Khai báo số lượng nhân sự mới (TechCorp).
Triển khai theo Giải pháp 1: while True + break.
"""

print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ ---")

while True:
    count_text = input("Vui lòng nhập số lượng nhân sự mới trong tháng: ").strip()

    # isdigit(): chỉ True khi toàn chữ số -> chặn số âm ("-5"), số lẻ, chữ, ô trống
    # and int(...) > 0: chặn số 0
    if count_text.isdigit() and int(count_text) > 0:
        new_employee_count = int(count_text)
        break   # dữ liệu hợp lệ -> thoát vòng lặp

    print("[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.\n")

print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài khoản cho {new_employee_count} nhân sự mới.")
print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
