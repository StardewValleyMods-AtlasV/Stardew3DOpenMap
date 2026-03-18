from PIL import Image
import os

def scale_down(image_path, output_path):
    img = Image.open(image_path)
    new_size = (img.width // 4, img.height // 4)
    scaled = img.resize(new_size, Image.NEAREST)
    scaled.save(output_path)
    print(f"  {img.width}x{img.height} -> {new_size[0]}x{new_size[1]}: {output_path}")

EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".webp", ".tiff"}

script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "Output")
os.makedirs(output_dir, exist_ok=True)

images = [
    f for f in os.listdir(script_dir)
    if os.path.splitext(f)[1].lower() in EXTENSIONS
]

if not images:
    print("no pics found in script directory")
else:
    print(f"found {len(images)} pic. saving to '{output_dir}'")
    for filename in images:
        input_path = os.path.join(script_dir, filename)
        output_path = os.path.join(output_dir, filename)
        scale_down(input_path, output_path)
    print("done")