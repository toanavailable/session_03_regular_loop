# Bài tập Python Session 3 - Vòng lặp cơ bản

Tổng hợp 6 bài tập thực hành về vòng lặp `for` và `while`, hàm `range()`, lệnh điều hướng vòng lặp `break` / `continue` và vòng lặp kiểm duyệt dữ liệu (validation loop). Bối cảnh chung là các hệ thống quản lý nhân sự / kế toán của doanh nghiệp.

## Danh sách bài tập

| STT | Bài tập | Loại bài | Kiến thức trọng tâm |
|---|---|---|---|
| 1 | [Vòng lặp cơ bản - Quản lý chấm công nhân viên](bai-1-quan-ly-cham-cong-nhan-vien/) | Bài tập tổng hợp | `for` + `range()`, `while True` + `break`, `if` đánh giá chuyên cần |
| 2 | [Sự cố tính toán quỹ lương](bai-2-su-co-tinh-toan-quy-luong/) | Vận dụng cơ bản - sửa lỗi legacy | Vị trí khởi tạo biến tích lũy (biến tổng) so với vòng lặp |
| 3 | [Sự cố tính thưởng Tết cho nhân viên](bai-3-su-co-tinh-thuong-tet/) | Vận dụng cơ bản - sửa lỗi legacy | Lệnh điều hướng `continue` trong vòng lặp |
| 4 | [Xây dựng hệ thống khởi tạo hồ sơ nhân sự](bai-4-khoi-tao-ho-so-nhan-su/) | Vận dụng chuyên sâu - thiết kế & code | `for` lặp đúng 3 lần, bẫy dữ liệu trống / toàn khoảng trắng, `continue` |
| 5 | [Xây dựng chức năng khai báo số lượng nhân sự mới](bai-5-khai-bao-so-luong-nhan-su-moi/) | Phân tích - so sánh 2 giải pháp | Vòng lặp validation: `while True` + `break` và `while` có điều kiện |
| 6 | [Xây dựng chức năng Cập nhật Hồ sơ & Đánh giá Năng lực](bai-6-cap-nhat-ho-so-danh-gia-nang-luc/) | Sáng tạo - thiết kế toàn bộ | Vòng lặp tổng + nhiều vòng lặp "bẫy chặn", ép kiểu an toàn, log `type()` |

Mỗi thư mục bài có `README.md` riêng (đề bài, phân tích, lời giải, kết quả kiểm thử) và mã nguồn Python. Hai bài sửa lỗi (bài 2, 3) có cả `script_legacy.py` (code gốc bị lỗi) và `script.py` (code đã sửa).

## Cách chạy

Yêu cầu Python 3.x. Vào thư mục bài cần chạy, ví dụ:

```bash
cd bai-1-quan-ly-cham-cong-nhan-vien
python cham_cong.py
```
