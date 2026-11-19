# Bài 4 - [Vận dụng chuyên sâu] Xây dựng hệ thống khởi tạo hồ sơ nhân sự

## Đề bài

Công ty TechCorp mỗi sáng thứ Hai tiếp nhận **chính xác 3 nhân sự mới**. Bộ phận HR nhập liệu thủ công vào sổ sách nên hay sai sót, khiến bộ phận IT không thể tự động tạo email và tài khoản hệ thống. Cần xây dựng module **"Kiosk Nhập liệu Nhân sự"**: tự động hỏi thông tin lần lượt từng người và xuất **"Hồ sơ Nhân sự Điện tử"**.

**Yêu cầu nghiệp vụ:**
- Giao diện dòng lệnh (CLI) tự động lặp quy trình nhập liệu **đúng 3 lần** (3 nhân viên).
- Mỗi lượt nhập 3 thông tin bắt buộc: **Mã nhân viên** (VD: `NV001`, `DEV009`), **Họ và tên**, **Phòng ban công tác** (VD: IT, Marketing, Kế toán).
- Nhập xong và hợp lệ thì in ngay **Phiếu Hồ sơ Điện tử** của người đó.
- In xong người này thì tự động chuyển sang người tiếp theo; hết 3 người thì kết thúc.

**Edge cases (bẫy dữ liệu):**
- **Bẫy 1:** Bỏ trống dữ liệu (nhấn Enter luôn).
- **Bẫy 2:** Dữ liệu rác: chỉ gõ toàn khoảng trắng.

Nếu **Mã nhân viên** HOẶC **Họ và tên** rơi vào bẫy thì **tuyệt đối không in phiếu**, chỉ in cảnh báo:
`[CẢNH BÁO] Dữ liệu trống hoặc không hợp lệ. Hủy tạo hồ sơ cho nhân viên này.`

## (1) Phân tích và thiết kế giải pháp

### Phân tích Input / Output

| Dữ liệu | Biến | Kiểu | Chuẩn hóa | Ràng buộc |
|---|---|---|---|---|
| Mã nhân viên | `employee_id` | `str` | `.strip().upper()` (`nv001` → `NV001`) | **Bắt buộc**, không rỗng |
| Họ và tên | `full_name` | `str` | Bỏ khoảng trắng thừa + `.title()` | **Bắt buộc**, không rỗng |
| Phòng ban | `department` | `str` | Bỏ khoảng trắng thừa | Nếu trống → ghi `Chưa phân bổ` |

**Output** mỗi lượt (một trong hai):
- Hợp lệ → **Phiếu Hồ sơ Điện tử** (Mã NV, Họ tên, Phòng ban).
- Không hợp lệ → dòng **[CẢNH BÁO]**, không in phiếu.

Cuối chương trình: dòng tổng kết số hồ sơ tạo thành công.

### Đề xuất giải pháp

| Kỹ thuật | Công dụng |
|---|---|
| `for employee_number in range(1, 4)` | Biết trước **đúng 3 lần** nên dùng `for`. Đánh số từ 1 để hiển thị "Nhân viên mới thứ 1/3" |
| `.strip()` / `" ".join(s.split())` | Biến chuỗi toàn khoảng trắng `"   "` thành chuỗi rỗng `""`. Nhờ vậy **Bẫy 1 và Bẫy 2 cùng bị bắt bằng một phép so sánh** `== ""` |
| `if employee_id == "" or full_name == ""` | Chỉ cần **một trong hai** trường lỗi là hủy, nên dùng toán tử `or` |
| `continue` | Hủy hồ sơ hiện tại, bỏ qua phần in phiếu, **chuyển ngay** sang nhân viên tiếp theo |
| Biến đếm `created_count` | Khởi tạo **trước** vòng lặp, `+= 1` mỗi khi tạo thành công, để tổng kết cuối chương trình |

### Thiết kế thuật toán (Pseudocode)

```
BẮT ĐẦU
    created_count ← 0
    LẶP employee_number TỪ 1 ĐẾN 3:
        NHẬP employee_id, full_name, department
        Chuẩn hóa: bỏ khoảng trắng thừa; employee_id IN HOA; full_name viết hoa chữ đầu

        NẾU employee_id rỗng HOẶC full_name rỗng THÌ
            IN "[CẢNH BÁO] Dữ liệu trống hoặc không hợp lệ. Hủy tạo hồ sơ cho nhân viên này."
            CHUYỂN sang nhân viên tiếp theo (continue)

        NẾU department rỗng THÌ department ← "Chưa phân bổ"
        created_count ← created_count + 1
        IN Phiếu Hồ sơ Điện tử (employee_id, full_name, department)
    HẾT LẶP
    IN "Hoàn tất! Đã tạo <created_count>/3 hồ sơ nhân sự."
KẾT THÚC
```

## (2) Triển khai code

File: [`khoi_tao_ho_so.py`](khoi_tao_ho_so.py)

```python
for employee_number in range(1, new_employee_count + 1):
    print(f"\n>>> Nhân viên mới thứ {employee_number}/{new_employee_count}")

    # --- Nhập dữ liệu ---
    employee_id = input("Mã nhân viên (VD: NV001, DEV009): ")
    full_name = input("Họ và tên (VD: Nguyễn Văn An): ")
    department = input("Phòng ban công tác (VD: IT, Marketing, Kế toán): ")

    # --- Chuẩn hóa: chuỗi toàn dấu cách sẽ thành chuỗi rỗng "" ---
    employee_id = employee_id.strip().upper()
    full_name = " ".join(full_name.split()).title()
    department = " ".join(department.split())

    # --- Kiểm tra bẫy dữ liệu: trống hoặc chỉ có khoảng trắng ---
    if employee_id == "" or full_name == "":
        print(warning_message)
        continue   # KHÔNG in phiếu, chuyển ngay sang nhân viên tiếp theo

    if department == "":
        department = "Chưa phân bổ"

    # --- In Phiếu Hồ sơ Điện tử ---
    created_count += 1
    ...
```

## Kết quả

Kiểm thử 3 lượt: nhân viên 1 hợp lệ (nhập chữ thường), nhân viên 2 có **mã toàn dấu cách** (Bẫy 2), nhân viên 3 **bỏ trống họ tên** (Bẫy 1):

```
=======================================================
          KIOSK NHẬP LIỆU NHÂN SỰ - TECHCORP
=======================================================

>>> Nhân viên mới thứ 1/3
Mã nhân viên (VD: NV001, DEV009): nv001
Họ và tên (VD: Nguyễn Văn An): nguyễn văn an
Phòng ban công tác (VD: IT, Marketing, Kế toán): IT
-------------------------------------------------------
                  PHIẾU HỒ SƠ ĐIỆN TỬ
-------------------------------------------------------
Mã nhân viên  : NV001
Họ và tên     : Nguyễn Văn An
Phòng ban     : IT
-------------------------------------------------------

>>> Nhân viên mới thứ 2/3
Mã nhân viên (VD: NV001, DEV009):
Họ và tên (VD: Nguyễn Văn An): Trần B
Phòng ban công tác (VD: IT, Marketing, Kế toán): Marketing
[CẢNH BÁO] Dữ liệu trống hoặc không hợp lệ. Hủy tạo hồ sơ cho nhân viên này.

>>> Nhân viên mới thứ 3/3
Mã nhân viên (VD: NV001, DEV009): DEV009
Họ và tên (VD: Nguyễn Văn An):
Phòng ban công tác (VD: IT, Marketing, Kế toán): Kế toán
[CẢNH BÁO] Dữ liệu trống hoặc không hợp lệ. Hủy tạo hồ sơ cho nhân viên này.

=======================================================
Hoàn tất! Đã tạo 1/3 hồ sơ nhân sự.
=======================================================
```

| # | Mã NV | Họ tên | Kết quả |
|---|---|---|---|
| 1 | `nv001` | `nguyễn văn an` | In phiếu: `NV001` - `Nguyễn Văn An` ✅ |
| 2 | `"   "` (toàn dấu cách) | Trần B | [CẢNH BÁO], không in phiếu ✅ |
| 3 | DEV009 | *(bỏ trống)* | [CẢNH BÁO], không in phiếu ✅ |
