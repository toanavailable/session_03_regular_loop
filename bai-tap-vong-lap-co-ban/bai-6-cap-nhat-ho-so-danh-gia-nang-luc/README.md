# Bài 6 - [Sáng tạo] Xây dựng chức năng Cập nhật Hồ sơ & Đánh giá Năng lực

## Đề bài

Tại TechCorp, quy trình đánh giá hiệu suất cuối năm đang gặp nhiều khó khăn vì dữ liệu từ các phòng ban gửi lên không đồng nhất, chứa nhiều lỗi (điểm KPI bằng chữ, lương âm, bỏ trống…). Giám đốc HR quyết định chuyển đổi số: thay vì nộp file Excel, bộ phận IT sẽ triển khai một **"Kiosk HR Tự Phục Vụ"** (giao diện Console) để Quản lý trực tiếp nhập liệu và cập nhật thông tin nhân sự của mình.

Kiosk phải được thiết kế cực kỳ thông minh:
- **Giao tiếp "bao bọc" (Foolproof UX):** hướng dẫn cực kỳ rõ ràng để không thể nhập sai định dạng.
- **Người gác cổng nghiêm khắc (Data Validation):** dùng vòng lặp để tạo ra các "bẫy chặn". Nếu nhập một số điểm KPI vô lý (VD: 10 điểm, trong khi thang điểm tối đa là 5), hệ thống tuyệt đối không lưu mà sẽ bắt vòng lặp nhập lại cho đến khi đúng thì thôi.
- **Hoạt động liên tục:** có một vòng lặp tổng bao ngoài để Quản lý nhập liên tục nhiều nhân viên mà không phải bật lại chương trình.

**Yêu cầu nghiệp vụ:**
- Thu thập thông tin cho từng nhân viên với ít nhất 5 trường dữ liệu (gồm thông tin cá nhân và chỉ số đánh giá).
- Kiểm tra dữ liệu đầu vào (validation) chặt chẽ bằng vòng lặp.
- Cho phép Quản lý nhập liên tục nhiều nhân viên.
- In ra **Hồ sơ Nhân sự Điện tử** và **Log hệ thống** sau mỗi lần nhập thành công.

**Ràng buộc:** một file Python duy nhất; Clean Code (`snake_case`, comment rõ từng khối chức năng); mỗi lần nhập sai thì báo lỗi rõ ràng và yêu cầu nhập lại trường đó.

## (1) Thiết kế kiến trúc và luồng dữ liệu

### Bảng thiết kế dữ liệu

Kiosk thu thập **5 trường**: 2 chuỗi và 3 số (thực/nguyên).

| # | Tên biến (snake_case) | Câu hỏi input | Kiểu dữ liệu | Điều kiện validation |
|---|---|---|---|---|
| 1 | `employee_id` | `1. Enter Employee ID (VD: DEV01):` | `str` | Không rỗng; tự chuyển IN HOA |
| 2 | `employee_name` | `2. Enter Full Name (VD: Nguyen Van A):` | `str` | Không rỗng; bỏ khoảng trắng thừa |
| 3 | `current_salary` | `3. Enter current Salary in VND (Number > 0, VD: 25000000):` | `float` | Là số **và** `> 0` |
| 4 | `performance_score` | `4. Enter Performance Score (1.0 to 5.0, VD: 4.5):` | `float` | Là số **và** `1.0 <= điểm <= 5.0` |
| 5 | `experience_years` | `5. Enter Year of Experience (Integer >= 0, VD: 3):` | `int` | Số nguyên `>= 0` |

### Luồng chương trình (Pseudocode)

```
BẮT ĐẦU
    IN màn hình chào "KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI"

    LẶP (vòng lặp tổng):
        // Mỗi trường là một vòng lặp "bẫy chặn" riêng
        LẶP: NHẬP employee_id     → NẾU không rỗng THÌ thoát, NGƯỢC LẠI báo lỗi
        LẶP: NHẬP employee_name   → NẾU không rỗng THÌ thoát, NGƯỢC LẠI báo lỗi
        LẶP: NHẬP current_salary
                NẾU không phải số      → báo lỗi, hỏi lại
                NẾU <= 0               → báo "Lương không thể là số âm hoặc bằng 0", hỏi lại
                NGƯỢC LẠI              → thoát
        LẶP: NHẬP performance_score
                NẾU không phải số      → báo lỗi, hỏi lại
                NẾU ngoài [1.0, 5.0]   → báo "Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0", hỏi lại
                NGƯỢC LẠI              → thoát
        LẶP: NHẬP experience_years → NẾU là số nguyên >= 0 THÌ thoát, NGƯỢC LẠI báo lỗi

        IN E-PROFILE (hồ sơ điện tử)
        IN IT SYSTEM LOG (tên biến | type(biến))

        HỎI "Do you want to enter another employee? (y/n)" (hỏi lại nếu không phải y/n)
        NẾU "n" THÌ IN "Đang tắt Kiosk... Tạm biệt!" và THOÁT vòng lặp tổng
KẾT THÚC
```

### Thiết kế câu hỏi `input()` (giảm lỗi người dùng)

- **Đánh số** từng câu (1. → 5.) để người dùng biết đang ở bước nào.
- Ghi rõ **đơn vị** (VND, years) và **ràng buộc ngay trong câu hỏi**: `(Number > 0)`, `(1.0 to 5.0)`, `(Integer >= 0)`.
- Luôn có **ví dụ cụ thể** `VD: ...`.
- Thông báo lỗi bắt đầu bằng `[!] Lỗi:` và **nói rõ sai ở đâu, phải nhập thế nào**, không chỉ báo chung chung "Sai rồi".
- Nhập sai trường nào thì **chỉ hỏi lại trường đó**, không bắt nhập lại từ đầu.

## (2) Triển khai code

File: [`kiosk_hr.py`](kiosk_hr.py), một file duy nhất, chia khối: Khởi tạo → Thu thập & kiểm tra → Hồ sơ điện tử → Log hệ thống → Hỏi tiếp tục.

### Vòng lặp "bẫy chặn" cho số thực (VD: lương)

```python
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
```

Giải thích:
- `isdigit()` không nhận dấu `.` và dấu `-`. Vì vậy trước khi kiểm tra, code tạm **bỏ dấu `-` ở đầu** và **bỏ một dấu `.`** (`replace(".", "", 1)`). Nếu phần còn lại toàn chữ số thì chuỗi gốc là một số hợp lệ (`-5000000`, `4.8`…), lúc đó mới ép kiểu `float()` an toàn mà **không crash**.
- Giữ lại dấu `-` khi ép kiểu, để số âm được nhận diện và báo **đúng lý do** "Lương không thể là số âm".
- `continue` quay lại đầu vòng lặp để hỏi lại; `break` chỉ chạy khi dữ liệu đã qua hết các "bẫy".

### Vòng lặp tổng và câu hỏi tiếp tục

```python
while True:                       # vòng lặp tổng
    ...                           # nhập 5 trường, in hồ sơ và log
    answer = input("\nDo you want to enter another employee? (y/n): ").strip().lower()
    while answer != "y" and answer != "n":
        answer = input("Vui lòng chỉ gõ 'y' hoặc 'n': ").strip().lower()

    if answer == "n":
        print("\nĐang tắt Kiosk... Tạm biệt!")
        break
```

## Kết quả

```
============================================================
          KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI
============================================================

[Nhập thông tin nhân viên]
1. Enter Employee ID (VD: DEV01): dev01
2. Enter Full Name (VD: Nguyen Van A): Nguyen  Van A
3. Enter current Salary in VND (Number > 0, VD: 25000000): -5000000
   [!] Lỗi: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!
3. Enter current Salary in VND (Number > 0, VD: 25000000): 25000000
4. Enter Performance Score (1.0 to 5.0, VD: 4.5): 6.5
   [!] Lỗi: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!
4. Enter Performance Score (1.0 to 5.0, VD: 4.5): 4.8
5. Enter Year of Experience (Integer >= 0, VD: 3): 3

============================================================
                     E-PROFILE CẬP NHẬT
============================================================
- ID         : DEV01
- Name       : Nguyen Van A
- Salary     : 25,000,000 VND
- KPI Score  : 4.8 / 5.0
- Experience : 3 years

============================================================
                       IT SYSTEM LOG
============================================================
employee_id        | <class 'str'>
employee_name      | <class 'str'>
current_salary     | <class 'float'>
performance_score  | <class 'float'>
experience_years   | <class 'int'>
============================================================

Do you want to enter another employee? (y/n): n

Đang tắt Kiosk... Tạm biệt!
```

**Bảng kiểm thử validation** (nhân viên thứ hai trong cùng lần chạy):

| Trường | Dữ liệu nhập | Kết quả |
|---|---|---|
| Employee ID | *(bỏ trống)* | `[!] Lỗi: Mã nhân viên không được để trống.` → hỏi lại |
| Full Name | *(bỏ trống)* | `[!] Lỗi: Họ và tên không được để trống.` → hỏi lại |
| Salary | `abc` | `[!] Lỗi: Lương phải là một con số` → hỏi lại (không crash) |
| Salary | `0` | `[!] Lỗi: Lương không thể là số âm hoặc bằng 0` → hỏi lại |
| KPI Score | `-1` | `[!] Lỗi: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!` → hỏi lại |
| KPI Score | `x` | `[!] Lỗi: Điểm KPI phải là một con số` → hỏi lại (không crash) |
| KPI Score | `1.0` | Hợp lệ (biên dưới) ✅ |
| Experience | `-2`, `2.5` | `[!] Lỗi: Số năm kinh nghiệm phải là số nguyên >= 0` → hỏi lại |
| Experience | `0` | Hợp lệ (biên dưới) ✅ |
| y/n | `k` | `Vui lòng chỉ gõ 'y' hoặc 'n'` → hỏi lại |
