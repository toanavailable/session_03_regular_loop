# Bài 3 - [Vận dụng cơ bản] Sự cố tính thưởng Tết cho nhân viên

## Đề bài

Vào dịp Tết, bộ phận Nhân sự (HR) cần tính và thông báo thưởng cho nhân viên thử việc. Kế toán lần lượt nhập **số ngày công** của từng nhân viên.

Quy định của công ty:
- Chỉ thưởng cho những nhân viên có ngày công > 0.
- Nhân viên nghỉ không lương cả tháng (0 ngày công) sẽ **không được thưởng** và chỉ nhận thông báo cảnh báo.

Sự cố: một nhân viên nghỉ ốm cả tháng có 0 ngày công. Hệ thống đã in cảnh báo trên màn hình HR, nhưng ngay sau đó vẫn tự động gửi email **"Chúc mừng bạn nhận được 0 VND tiền thưởng!"**. Email này khiến nhân viên hiểu lầm là công ty đang mỉa mai họ. Bộ phận IT phát hiện cấu trúc vòng lặp bị **thiếu lệnh điều hướng**: chương trình biết ngày công bằng 0 nhưng vẫn gửi thông báo.

Yêu cầu: (1) dò luồng thực thi khi nhập số ngày công = 0, giải thích vì sao hệ thống vẫn chạy xuống phần tính thưởng và gửi email dù đã vào nhánh cảnh báo, chỉ ra vấn đề liên quan đến cấu trúc điều kiện trong vòng lặp; (2) sửa code để khi số ngày công = 0, hệ thống **chỉ in cảnh báo và chuyển ngay sang nhân viên tiếp theo**, tuyệt đối không tính thưởng và không gửi email.

## Mã nguồn hiện tại (legacy)

File: [`script_legacy.py`](script_legacy.py) *(gõ lại từ ảnh đề bài)*

```python
print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

# Vòng lặp chạy đúng 3 lần cho 3 nhân viên
for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")

    # Yêu cầu kế toán nhập dữ liệu
    working_days = int(input("Nhập số ngày công trong tháng: "))

    # Kiểm tra điều kiện
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")

    bonus_amount = working_days * 200000
    print("-> Đã gửi email: Chúc mừng nhận được", bonus_amount, "VND tiền thưởng!")
    print("----------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")
```

## (1) Phân tích lỗi

### Dò luồng thực thi với `working_days = 0` (nhân viên số 2)

| Bước | Câu lệnh | Kết quả |
|---|---|---|
| 1 | `working_days = int(input(...))` | `working_days = 0` |
| 2 | `if working_days == 0:` | `0 == 0` → **True** |
| 3 | `print("CẢNH BÁO: ...")` | In cảnh báo ✅ |
| 4 | *Hết khối `if`, chương trình chạy tiếp xuống dòng kế tiếp* | |
| 5 | `bonus_amount = working_days * 200000` | `bonus_amount = 0` ❌ |
| 6 | `print("-> Đã gửi email: ...")` | Gửi email "nhận được 0 VND tiền thưởng!" ❌ |
| 7 | Sang lượt lặp tiếp theo | |

### Vì sao vẫn chạy xuống phần tính thưởng?

- Khối `if` chỉ chứa **một** câu lệnh: `print("CẢNH BÁO...")`. Các dòng `bonus_amount = ...` và `print("-> Đã gửi email...")` thụt lề **ngang hàng với `if`**, tức là **nằm ngoài** khối `if`.
- `if` không phải là lệnh "dừng lại". Sau khi chạy xong khối của mình, Python **tiếp tục thực hiện các lệnh phía sau** như bình thường.
- Không có nhánh `else` và cũng không có lệnh điều hướng vòng lặp (`continue`) để **bỏ qua** phần còn lại của lượt lặp. Vì vậy phần tính thưởng và gửi email **luôn chạy với mọi nhân viên**, kể cả người có 0 ngày công.

Kết luận: đây là **lỗi logic** do thiếu lệnh điều hướng vòng lặp. Đề đã ghi rõ "cấu trúc vòng lặp bị thiếu lệnh điều hướng".

## (2) Sửa lỗi

Dùng lệnh **`continue`**: bỏ qua toàn bộ phần còn lại của lượt lặp hiện tại và **chuyển ngay sang lượt tiếp theo** (nhân viên tiếp theo).

File: [`script.py`](script.py)

```python
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
```

Thay đổi:
1. **Sửa lỗi chính:** thêm `continue` cuối khối `if working_days == 0`.
2. Đưa mức thưởng mỗi ngày công vào biến `bonus_per_day`, tránh "số ma thuật" nằm rải rác trong code.
3. Định dạng tiền thưởng có dấu phân cách hàng nghìn.

> **Cách sửa khác:** đưa phần tính thưởng và gửi email vào nhánh `else:`. Kết quả tương đương, nhưng `continue` đúng với gợi ý "thiếu lệnh điều hướng vòng lặp". Cách này cũng giúp phần xử lý chính không bị thụt lề thêm một cấp.

## Kết quả

Kiểm thử với 3 nhân viên có ngày công lần lượt **20, 0, 15**:

| Nhân viên | Ngày công | Legacy | Sau khi sửa |
|---|---|---|---|
| 1 | 20 | Gửi email 4000000 VND | Gửi email 4,000,000 VND ✅ |
| 2 | **0** | Cảnh báo **+ gửi email 0 VND** ❌ | **Chỉ cảnh báo**, không gửi email ✅ |
| 3 | 15 | Gửi email 3000000 VND | Gửi email 3,000,000 VND ✅ |

```
--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---
--- Đang xử lý nhân viên số 1 ---
Nhập số ngày công trong tháng: 20
-> Đã gửi email: Chúc mừng nhận được 4,000,000 VND tiền thưởng!
----------------------------------------

--- Đang xử lý nhân viên số 2 ---
Nhập số ngày công trong tháng: 0
CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.
----------------------------------------

--- Đang xử lý nhân viên số 3 ---
Nhập số ngày công trong tháng: 15
-> Đã gửi email: Chúc mừng nhận được 3,000,000 VND tiền thưởng!
----------------------------------------

Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!
```
