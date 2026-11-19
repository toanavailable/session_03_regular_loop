# Bài 1 - [Bài tập tổng hợp] Vòng lặp cơ bản - Quản lý chấm công nhân viên

## Đề bài

Một công ty nhỏ cần chương trình Python chạy trên Console để quản lý chấm công nhân viên văn phòng. Chương trình cho phép:

1. **Nhập số lượng nhân viên** cần quản lý.
2. **Nhập thông tin từng nhân viên:** tên nhân viên, số ngày đi làm.
3. **Hiển thị lại thông tin** ngay sau khi nhập xong mỗi nhân viên.
4. **Đánh giá chuyên cần:** dưới 20 ngày → `Cần cải thiện chuyên cần`; từ 20 ngày trở lên → `Nhân viên chuyên cần tốt`.
5. **Tiếp tục hoặc kết thúc:** nhập `y` thì chương trình chạy lại, nhập `n` thì in `Chương trình kết thúc`.

Kiến thức ôn tập: vòng lặp `for` và `while`, `range()`, duyệt dữ liệu bằng vòng lặp, `if` kiểm tra điều kiện, `break` để kết thúc chương trình.

## Phân tích

| Dữ liệu | Biến | Kiểu |
|---|---|---|
| Số lượng nhân viên | `employee_count` | `int` |
| Tên nhân viên | `employee_name` | `str` |
| Số ngày đi làm | `working_days` | `int` |
| Lựa chọn tiếp tục | `answer` | `str` (`"y"` / `"n"`) |

Chương trình cần **hai vòng lặp lồng nhau**:

| Vòng lặp | Loại | Lý do chọn |
|---|---|---|
| Ngoài: chạy lại chương trình | `while True` + `break` | **Không biết trước** người dùng muốn chạy bao nhiêu lượt; chỉ dừng khi họ nhập `n` |
| Trong: nhập từng nhân viên | `for ... in range(1, employee_count + 1)` | **Biết trước** số lần lặp = số lượng nhân viên vừa nhập |

`range(1, employee_count + 1)` cho số thứ tự nhân viên chạy từ 1 thay vì 0. Phải `+ 1` vì `range` không gồm giá trị kết thúc, nếu quên sẽ thiếu mất nhân viên cuối.

## Lời giải

File: [`cham_cong.py`](cham_cong.py)

```python
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
```

Giải thích:
- `while True` tạo vòng lặp chạy mãi; lệnh **`break`** là lối thoát duy nhất, chỉ chạy khi người dùng nhập `n`.
- Khi nhập `y`, vòng `while True` quay lại đầu, hỏi lại số lượng nhân viên.
- Vòng `while` nhỏ ở cuối giúp chương trình **hỏi lại** nếu người dùng gõ nhầm (VD: `maybe`) thay vì hiểu sai ý. `.lower()` để `Y`/`N` viết hoa cũng được chấp nhận.

## Kết quả

```
Nhập số lượng nhân viên: 2

Nhân viên 1
Tên nhân viên: Thiên Long
Số ngày đi làm: 21
Thông tin nhân viên:
Tên: Thiên Long
Số ngày đi làm: 21
Nhân viên chuyên cần tốt

Nhân viên 2
Tên nhân viên: Anh Đào
Số ngày đi làm: 19
Thông tin nhân viên:
Tên: Anh Đào
Số ngày đi làm: 19
Cần cải thiện chuyên cần

Tiếp tục chương trình? (y/n): y

Nhập số lượng nhân viên: 1

Nhân viên 1
Tên nhân viên: Thu
Số ngày đi làm: 30
Thông tin nhân viên:
Tên: Thu
Số ngày đi làm: 30
Nhân viên chuyên cần tốt

Tiếp tục chương trình? (y/n): n
Chương trình kết thúc
```

Kết quả khớp với kết quả mong muốn của đề.
