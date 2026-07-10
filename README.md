# 🖼️ Python Image Tool

Dự án này là một công cụ xử lý hình ảnh tự động bằng Python (sử dụng thư viện `Pillow`). Chức năng chính hiện tại là **thay đổi kích thước (resize) hàng loạt** các hình ảnh có trong thư mục `input_images` và tự động lưu kết quả vào thư mục `output_images`.

Dự án được thiết kế với cấu trúc module, dễ dàng mở rộng để thêm các tính năng xử lý ảnh khác trong tương lai (ví dụ: crop, watermark, nén ảnh...).

---

## 📁 Cấu trúc thư mục

```
image-with-python/
├── venv/                     # môi trường ảo Python
├── src/                      # chứa toàn bộ mã nguồn
│   ├── __init__.py
│   ├── main.py               # entrypoint chính
│   ├── utils/                # thư mục dùng chung
│   │   ├── __init__.py
│   │   └── file_utils.py     # ví dụ: hàm load/save/check file
│   └── image_tools/          # nhóm tiện ích về hình ảnh
│       ├── __init__.py
│       └── resize/           # module riêng cho chức năng resize
│           ├── __init__.py
│           └── resize_images.py
├── input_images/             # chứa ảnh gốc
├── output_images/            # chứa ảnh sau khi xử lý
├── requirements.txt          # các gói cần cài
└── README.md
```

---

## ⚙️ Cách khởi tạo dự án

### 1️⃣ Tạo môi trường ảo

```bash
python -m venv venv
source venv/Scripts/activate    # Windows (Git Bash)
# hoặc: source venv/bin/activate   # Linux/macOS
```

### 2️⃣ Cài thư viện cần thiết

```bash
pip install pillow
```

Lưu lại danh sách package:

```bash
pip freeze > requirements.txt
```

---

## ✍️ 3️⃣ Nội dung file `src/image_tools/resize/resize_images.py`

```python
from PIL import Image
import os

def resize_images(input_dir, output_dir, width, height):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(input_dir, filename)

            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_{int(width)}x{int(height)}{ext}"
            output_path = os.path.join(output_dir, new_filename)

            with Image.open(input_path) as img:
                resized_img = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)
                resized_img.save(output_path)

            print(f"✅ Resized: {filename} → {new_filename}")

    print("🎉 Done! All images resized successfully.")

```

---

## ✍️ 4️⃣ File `src/main.py`

```python
from image_tools.resize.resize_images import resize_images

if __name__ == "__main__":
    input_dir = "input_images"
    output_dir = "output_images"
    width = 90
    height = 80

    resize_images(input_dir, output_dir, width, height)
```

---

## 🚀 5️⃣ Chạy chương trình

Từ thư mục gốc (`image-with-python/`):

```bash
python src/main.py
```

---

## 💡 Ưu điểm của cấu trúc này

* Mỗi **chức năng riêng (resize, crop, watermark, convert format, v.v.)** có thể nằm trong **folder riêng** trong `image_tools/`.
* Dễ **import module** và **mở rộng thêm tiện ích** sau này mà không rối.
* Dễ đóng gói thành **package Python nội bộ** hoặc chạy lệnh CLI nếu bạn muốn nâng cấp thành tool thực thụ.

---

Bạn có muốn tôi viết thêm **CLI command (dùng argparse)** để bạn có thể chạy như:

```bash
python src/main.py resize --width 90 --height 80
```
