from PIL import Image
from datetime import datetime
import os
from .image_processor import ImageProcessor

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = Image.open(image_path).convert("RGB")

    def rotate_90_clockwise(self):#Поворачивает изображение на 90° по часовой стрелке.
        self.image = self.image.rotate(-90, expand=True)

    def save_as_png_with_date(self):#Сохраняет изображение в формате PNG с датой в имени файла.
        dir_name = os.path.dirname(self.image_path)
        base_name = os.path.basename(self.image_path)
        name, _ = os.path.splitext(base_name)

        date_str = datetime.now().strftime("%Y-%m-%d")
        new_name = f"{name}_{date_str}.png"
        output_path = os.path.join(dir_name, new_name)

        self.image.save(output_path, "PNG")
        return output_path

    def get_processor(self):#Возвращает объект ImageProcessor с текущим
        return ImageProcessor(self.image)