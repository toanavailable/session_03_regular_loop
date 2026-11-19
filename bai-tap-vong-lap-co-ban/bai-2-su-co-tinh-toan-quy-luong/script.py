print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

employee_count = 3

# Khởi tạo biến tổng MỘT LẦN DUY NHẤT, đặt TRƯỚC vòng lặp
# để giá trị được giữ lại và cộng dồn qua các lần lặp
total_budget = 0

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, employee_count + 1):
    print("Đang xử lý nhân viên số", employee_number)

    # Nhập mức lương
    salary = int(input("  Nhập mức lương (VND): "))

    # Cộng dồn lương vào ngân sách tổng
    total_budget += salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình (nằm NGOÀI vòng lặp)
print(f"=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ: {total_budget:,} VND")
