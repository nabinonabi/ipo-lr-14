from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image.copy()

    def apply_blur_filter(self):#Применяет фильтр размытия
        self.image = self.image.filter(ImageFilter.BLUR)

    def add_watermark(self, text="Вариант 5"):#Добавляет полупрозрачный водяной знак в левый верхний угол.
        txt_layer = Image.new("RGBA", self.image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)

        try:
            font = ImageFont.truetype("arial.ttf", 32)
        except IOError:
            font = ImageFont.load_default()

        draw.text((10, 10), text, fill=(255, 255, 255, 128), font=font)

        if self.image.mode != "RGBA":
            self.image = self.image.convert("RGBA")
        combined = Image.alpha_composite(self.image, txt_layer)
        self.image = combined.convert("RGB")

    def get_image(self):#Возвращает обработанное изображение.
        return self.image