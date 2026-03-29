import sys
import os
from PIL import Image

def process_image(input_path):
    try:
        # checking is there file or not
        if not os.path.exists(input_path):
            print(f"Error: File {input_path} not found")
            return

        img = Image.open(input_path)
        target_size = (1280, 800)
        
        
        resample_filter = getattr(Image, 'Resampling', Image).LANCZOS

        img_ratio = img.width / img.height
        target_ratio = target_size[0] / target_size[1]
        
        
        if img_ratio > target_ratio:
            new_height = target_size[1]
            new_width = int(new_height * img_ratio)
            img = img.resize((new_width, new_height), resample_filter)
            left = (new_width - target_size[0]) / 2
            img = img.crop((left, 0, left + target_size[0], target_size[1]))
        else:
            new_width = target_size[0]
            new_height = int(new_width / img_ratio)
            img = img.resize((new_width, new_height), resample_filter)
            top = (new_height - target_size[1]) / 2
            img = img.crop((0, top, target_size[0], top + target_size[1]))
        
        # saving file to _fixe d.png 
        filename = os.path.splitext(input_path)[0]
        output_path = f"{filename}_fixed.png"
        
        img = img.convert("RGB")
        img.save(output_path, "PNG")
        print(f"Success! Saved as: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_image(sys.argv[1])
    else:
        print("Usage: python3 fixer.py <image_name>")
