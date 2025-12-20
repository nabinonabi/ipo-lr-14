from PIL import Image
from datetime import datetime
import os
from .image_processor import ImageProcessor

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path).convert("RGB")

    def resize_to_50_percent(self):
        
        width, height = self.image.size
        new_size = (int(width * 0.5), int(height * 0.5))
        self.image = self.image.resize(new_size, Image.Resampling.LANCZOS)

    def save_with_date_suffix(self, suffix=""):
        
        dir_name = os.path.dirname(self.image_path)
        base_name = os.path.basename(self.image_path)
        name, ext = os.path.splitext(base_name)

        date_str = datetime.now().strftime("%Y-%m-%d")
        new_name = f"{name}_{date_str}{suffix}{ext}"
        output_path = os.path.join(dir_name, new_name)

        self.image.save(output_path)
        return output_path

    def get_processor(self):
        
        return ImageProcessor(self.image)