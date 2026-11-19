print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

bonus_per_day = 200000   # tiền thưởng cho mỗi ngày công (VND)

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện: nghỉ cả tháng -> chỉ cảnh báo rồi chuyển ngay sang nhân viên tiếp theo
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("----------------------------------------\n")
        continue   # bỏ qua phần còn lại của lượt này: KHÔNG tính thưởng, KHÔNG gửi email

    bonus_amount = working_days * bonus_per_day
    print(f"-> Đã gửi email: Chúc mừng nhận được {bonus_amount:,} VND tiền thưởng!")
    print("----------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
