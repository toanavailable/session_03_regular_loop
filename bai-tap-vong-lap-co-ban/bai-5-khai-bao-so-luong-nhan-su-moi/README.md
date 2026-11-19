# Bài 5 - [Phân tích] Xây dựng chức năng khai báo số lượng nhân sự mới

## Đề bài

Tại bộ phận Tuyển dụng của TechCorp, đầu mỗi tháng chuyên viên nhân sự phải khai báo **"Số lượng nhân viên mới"** vào phần mềm để bộ phận IT chuẩn bị máy tính và tạo tài khoản email.

Phần mềm hiện tại bị lỗi: nó cho phép nhập số lượng là số âm (VD: `-5`) hoặc số `0`. Khi dữ liệu này được gửi sang phòng IT, hệ thống tự động cấp phát tài sản bị lỗi (crash) vì không thể tạo "-5 cái máy tính".

Nhiệm vụ: viết đoạn code kiểm duyệt dữ liệu đầu vào, dùng vòng lặp để **"ép"** chuyên viên HR phải nhập đúng số lượng hợp lệ thì mới cho đi tiếp.

**Yêu cầu nghiệp vụ:**
- Hệ thống yêu cầu: `"Vui lòng nhập số lượng nhân sự mới trong tháng: "`.
- **Điều kiện hợp lệ:** bắt buộc là **số nguyên lớn hơn 0** (1, 3, 10…).
- **Cơ chế hoạt động:** nhập số `<= 0` thì báo lỗi và **tự động yêu cầu nhập lại ngay lập tức**. Chỉ dừng vòng lặp và in thông báo "Ghi nhận thành công" khi nhập số hợp lệ.

**Edge cases (bẫy dữ liệu):**
- **Bẫy 1 - Nhập số 0:** HR nghĩ tháng này không có ai nên nhập 0, nhưng nghiệp vụ yêu cầu nếu không có ai thì không mở phần mềm này.
- **Bẫy 2 - Nhập số âm:** HR gõ nhầm phím, VD `-3`.

## (1) Phân tích và đề xuất giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu ban đầu | Kiểu mong muốn | Cần xử lý gì? |
|---|---|---|---|---|
| Số lượng nhân sự mới | `count_text` → `new_employee_count` | `str` (từ `input()`) | `int` | Bỏ khoảng trắng; kiểm tra là số nguyên dương **trước** khi ép kiểu |

**Output:**
- Không hợp lệ: `[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.` rồi hỏi lại.
- Hợp lệ: `[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài khoản cho <N> nhân sự mới.` và `--- CHƯƠNG TRÌNH KẾT THÚC ---`.

**Điều kiện hợp lệ** viết bằng Python: `count_text.isdigit() and int(count_text) > 0`
- `isdigit()` chỉ `True` khi chuỗi **toàn chữ số**, nên chặn được số âm `-3` (vì dấu `-` không phải chữ số), số lẻ `2.5`, chữ `abc` và ô trống. Nhờ vậy chương trình **không crash** khi gõ nhầm.
- `int(count_text) > 0` chặn số `0`.
- Toán tử `and` **dừng sớm**: nếu `isdigit()` đã `False` thì Python không chạy `int(...)` nữa, nên không bị lỗi `ValueError`.

### Đề xuất 2 giải pháp vòng lặp kiểm duyệt (validation loop)

**Giải pháp 1: `while True` + `break`**: lặp vô hạn, hỏi trong vòng lặp; hợp lệ thì `break` thoát ra.

```python
while True:
    count_text = input("Vui lòng nhập số lượng nhân sự mới trong tháng: ").strip()
    if count_text.isdigit() and int(count_text) > 0:
        new_employee_count = int(count_text)
        break
    print("[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.\n")
```

**Giải pháp 2: `while` với điều kiện lỗi (nhập trước, kiểm tra sau)**: hỏi một lần **trước** vòng lặp; vòng lặp chạy **chừng nào dữ liệu còn sai**, mỗi lượt báo lỗi và hỏi lại.

```python
count_text = input("Vui lòng nhập số lượng nhân sự mới trong tháng: ").strip()
while not (count_text.isdigit() and int(count_text) > 0):
    print("[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.\n")
    count_text = input("Vui lòng nhập số lượng nhân sự mới trong tháng: ").strip()
new_employee_count = int(count_text)
```

### Bảng so sánh

| Tiêu chí | Giải pháp 1: `while True` + `break` | Giải pháp 2: `while` có điều kiện |
|---|---|---|
| **Độ ngắn gọn của code** | ✅ Câu `input()` chỉ viết **1 lần** | ❌ Câu `input()` bị **lặp lại 2 lần** (trước và trong vòng lặp); sửa câu nhắc phải sửa 2 chỗ |
| **Mức độ dễ đọc (với người mới học)** | ✅ Đọc từ trên xuống như ngôn ngữ tự nhiên: "hỏi → nếu đúng thì thoát → nếu sai thì báo lỗi". Điều kiện viết ở dạng **khẳng định** (hợp lệ) | ❌ Điều kiện phải viết ở dạng **phủ định** `not (...)`, dễ nhầm. Người mới hay quên câu `input()` bên trong và gây **lặp vô hạn** |
| Điểm yếu | `while True` trông giống lặp vô hạn, phải đảm bảo luôn có `break` | Ưu điểm: điều kiện dừng nằm ngay trên dòng `while` nên thấy ngay khi nào vòng lặp kết thúc |

### Chốt lựa chọn: **Giải pháp 1 (`while True` + `break`)**

- Không lặp code: câu hỏi và cách xử lý nằm **một chỗ** nên dễ bảo trì.
- Điều kiện hợp lệ viết **thuận** (giống hệt quy định nghiệp vụ "số nguyên > 0") nên dễ đọc, dễ kiểm tra với yêu cầu.
- Đây là mẫu chuẩn, phổ biến cho bài toán "nhập lại đến khi đúng", sau này có thể tái sử dụng cho mọi ô nhập liệu khác.

## (2) Triển khai code

File: [`khai_bao_nhan_su.py`](khai_bao_nhan_su.py), triển khai theo **Giải pháp 1**.

```python
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
```

## Kết quả

```
--- HỆ THỐNG KHAI BÁO NHÂN SỰ ---
Vui lòng nhập số lượng nhân sự mới trong tháng: -5
[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.

Vui lòng nhập số lượng nhân sự mới trong tháng: 0
[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.

Vui lòng nhập số lượng nhân sự mới trong tháng: abc
[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.

Vui lòng nhập số lượng nhân sự mới trong tháng: 2.5
[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.

Vui lòng nhập số lượng nhân sự mới trong tháng:
[LỖI] Số lượng không hợp lệ. Vui lòng nhập một số lớn hơn 0.

Vui lòng nhập số lượng nhân sự mới trong tháng: 3
[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài khoản cho 3 nhân sự mới.
--- CHƯƠNG TRÌNH KẾT THÚC ---
```

| Dữ liệu nhập | Kết quả |
|---|---|
| `-5` (Bẫy 2) | [LỖI], hỏi lại ✅ |
| `0` (Bẫy 1) | [LỖI], hỏi lại ✅ |
| `abc` | [LỖI], hỏi lại (không crash) ✅ |
| `2.5` | [LỖI], hỏi lại (không crash) ✅ |
| *(bỏ trống)* | [LỖI], hỏi lại (không crash) ✅ |
| `3` | [THÀNH CÔNG], kết thúc ✅ |
