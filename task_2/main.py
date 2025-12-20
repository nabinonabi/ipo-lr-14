from image_tools.image_handler import ImageHandler

def main():
    print("Обработка изображения Вариант 5")
    image_path = input("Введите путь к изображению: ").strip()

    try:
        handler = ImageHandler(image_path)
        print("Изображение успешно загружено.")

        
        handler.resize_to_50_percent()
        print("Изображение уменьшено до 50%.")

        
        processor = handler.get_processor()
        print("Применяем фильтр 'Эмбосс' и добавляем водяной знак")

        processor.apply_emboss_filter()
        processor.add_watermark("Вариант 5")

        
        handler.image = processor.get_image()

        
        output_path = handler.save_with_date_suffix("_processed")
        print(f"Обработанное изображение сохранено как: {output_path}")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()