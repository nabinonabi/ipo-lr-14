from PIL import Image, ImageFilter, ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image):
        self.image = image.copy()

    def apply_emboss_filter(self):
        
        self.image = self.image.filter(ImageFilter.EMBOSS)

    def add_watermark(self, text="Вариант 5"):
        
        watermark = self.image.copy()
        draw = ImageDraw.Draw(watermark)

        try:
            font = ImageFont.truetype("arial.ttf", 36)
        except IOError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        x = self.image.width - text_width - 10
        y = self.image.height - text_height - 10

        
        txt_layer = Image.new("RGBA", self.image.size, (255, 255, 255, 0))
        txt_draw = ImageDraw.Draw(txt_layer)
        txt_draw.text((x, y), text, fill=(255, 255, 255, 128), font=font)

        if self.image.mode != "RGBA":
            self.image = self.image.convert("RGBA")
        combined = Image.alpha_composite(self.image, txt_layer)
        self.image = combined.convert("RGB")

    def get_image(self):
        
        return self.image