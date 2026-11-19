"""[Bài tập tổng hợp] Vòng lặp cơ bản - Quản lý chấm công nhân viên văn phòng."""

min_working_days = 20   # từ 20 ngày trở lên là chuyên cần tốt

# Vòng lặp ngoài: chạy lại chương trình cho đến khi người dùng chọn "n"
while True:
    employee_count = int(input("\nNhập số lượng nhân viên: "))

    # Vòng lặp trong: nhập lần lượt từng nhân viên (biết trước số lần -> dùng for)
    for employee_number in range(1, employee_count + 1):
        print(f"\nNhân viên {employee_number}")
        employee_name = input("Tên nhân viên: ").strip()
        working_days = int(input("Số ngày đi làm: "))

        # Hiển thị thông tin vừa nhập
        print("Thông tin nhân viên:")
        print(f"Tên: {employee_name}")
        print(f"Số ngày đi làm: {working_days}")

        # Đánh giá chuyên cần
        if working_days < min_working_days:
            print("Cần cải thiện chuyên cần")
        else:
            print("Nhân viên chuyên cần tốt")

    # Hỏi tiếp tục hay kết thúc (hỏi lại nếu gõ khác y/n)
    answer = input("\nTiếp tục chương trình? (y/n): ").strip().lower()
    while answer != "y" and answer != "n":
        answer = input("Vui lòng chỉ nhập y hoặc n: ").strip().lower()

    if answer == "n":
        print("Chương trình kết thúc")
        break
