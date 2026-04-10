import os
from PIL import Image,ImageOps
input_dir = 'HW 4_Images'
targets = {
    'Clipped_Images_1280x1280': (1280, 1280),
    'Clipped_Images_640': (640, 640)
}
valid_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
if not os.path.exists(input_dir):
    print(f"Input directory '{input_dir}' does not exist.")
else:
    files = [f for f in os.listdir(input_dir) if f.endswith(valid_extensions)]

    for folder_name, size in targets.items():
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        print(f"\n Processing images for target size: {size[0]}x{size[1]} images in {folder_name} ")

        for filename in files:
            with Image.open(os.path.join(input_dir, filename)) as img:
                clipped_img = ImageOps.fit(img, size, method=Image.LANCZOS)
                clipped_img.save(os.path.join(folder_name, filename))
                print(f"Saved {filename} to {folder_name}")
    print("\n All images have been processed and saved to the respective folders.")