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
