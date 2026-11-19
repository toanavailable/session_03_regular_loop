# Bài 2 - [Vận dụng cơ bản] Sự cố tính toán quỹ lương

## Đề bài

Phòng Kế toán cần tính **tổng quỹ lương** tháng này cho 3 nhân viên. Kế toán nhập mức lương từng người (3 lần nhập), sau đó hệ thống cộng dồn và in ra **"Tổng ngân sách"** để chuẩn bị rút tiền ngân hàng.

Sự cố:
- Lương nhân viên 1: 5.000.000 VND
- Lương nhân viên 2: 4.000.000 VND
- Lương nhân viên 3: 6.000.000 VND
- **Mong đợi:** Tổng quỹ lương = **15.000.000 VND**
- **Thực tế hệ thống in ra:** **6.000.000 VND** (chỉ lấy lương của người cuối cùng)

Chương trình chạy bình thường, không lỗi cú pháp, nhưng kết quả hoàn toàn sai.

Yêu cầu: (1) dò luồng thực thi, giải thích vì sao `total_budget` không cộng dồn mà chỉ giữ giá trị lần nhập cuối, chỉ ra lỗi logic về vị trí đặt biến trong vòng lặp; (2) sửa code để tính đúng tổng quỹ lương.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py) *(gõ lại từ ảnh đề bài)*

```python
print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

# Vòng lặp chạy 3 lần để nhập lương cho 3 nhân viên
for employee_number in range(1, 4):

    # Khởi tạo biến chứa ngân sách tổng
    total_budget = 0

    print("Đang xử lý nhân viên số", employee_number)
    # Nhập mức lương
    salary = int(input("  Nhập mức lương (VND): "))

    # Thực hiện thao tác cộng dồn tiền vào ngân sách
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VND")
```

## (1) Phân tích lỗi

### Dò luồng thực thi (trace code)

| Lượt lặp | `total_budget = 0` | Nhập `salary` | `total_budget = total_budget + salary` |
|---|---|---|---|
| 1 | `total_budget` = **0** | 5000000 | 0 + 5000000 = **5000000** |
| 2 | `total_budget` bị đặt lại = **0** ❌ | 4000000 | 0 + 4000000 = **4000000** |
| 3 | `total_budget` bị đặt lại = **0** ❌ | 6000000 | 0 + 6000000 = **6000000** |
| Sau vòng lặp | | | In ra `6000000` ❌ |

### Vì sao `total_budget` không cộng dồn?

- Dòng `total_budget = 0` nằm **bên trong** vòng lặp (thụt lề cùng cấp với các lệnh trong `for`), nên nó **chạy lại ở đầu mỗi lượt lặp**.
- Mỗi lượt, số tiền đã cộng dồn từ các lượt trước bị **xóa về 0**, rồi chỉ cộng thêm lương của người đang nhập.
- Đến khi vòng lặp kết thúc, `total_budget` chỉ còn lương của **người cuối cùng** (6.000.000).

### Lỗi logic kinh điển: khởi tạo biến tích lũy bên trong vòng lặp

Biến tích lũy (biến tổng, biến đếm) phải được **khởi tạo một lần duy nhất, TRƯỚC vòng lặp**. Bên trong vòng lặp chỉ **cập nhật** biến đó. Python không báo lỗi vì về cú pháp, gán lại `total_budget = 0` nhiều lần là hoàn toàn hợp lệ. Lỗi nằm ở **vị trí** của câu lệnh, tức là ở logic.

## (2) Sửa lỗi

File: [`script.py`](script.py)

```python
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
```

Thay đổi:
1. **Sửa lỗi chính:** chuyển `total_budget = 0` ra **trước** vòng lặp.
2. Dùng toán tử gán kết hợp `total_budget += salary` (tương đương `total_budget = total_budget + salary`), gọn hơn.
3. Đưa số nhân viên vào biến `employee_count` để dễ thay đổi.
4. Định dạng số tiền có dấu phân cách hàng nghìn `{total_budget:,}` (`15000000` → `15,000,000`) để kế toán dễ đọc.

## Kết quả

Trace sau khi sửa:

| Lượt lặp | `total_budget` trước | `salary` | `total_budget` sau |
|---|---|---|---|
| (trước vòng lặp) | | | 0 |
| 1 | 0 | 5000000 | 5000000 |
| 2 | 5000000 | 4000000 | 9000000 |
| 3 | 9000000 | 6000000 | **15000000** ✅ |

```
--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---
Đang xử lý nhân viên số 1
  Nhập mức lương (VND): 5000000
Đang xử lý nhân viên số 2
  Nhập mức lương (VND): 4000000
Đang xử lý nhân viên số 3
  Nhập mức lương (VND): 6000000
=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ: 15,000,000 VND
```
