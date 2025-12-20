from image_tools.image_handler import ImageHandler

def main():
    print("Обработка изображения Вариант 5")
    image_path = input("Введите путь к изображению: ").strip()

    try:
        handler = ImageHandler(image_path)
        print("Изображение загружено.")

        
        handler.rotate_90_clockwise()
        print("Изображение повернуто на 90° по часовой стрелке.")

       
        processor = handler.get_processor()
        print("Применяем фильтр и добавляем водяной знак")

        processor.apply_blur_filter()
        processor.add_watermark("Вариант 5")

        
        handler.image = processor.get_image()

        
        output_path = handler.save_as_png_with_date()
        print(f"Обработанное изображение сохранено как: {output_path}")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()