# file_operations.py - чтение и запись файлов

def read_cars_from_file(filename):
    """Чтение базы автомобилей из файла."""
    cars = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(',')
                if len(parts) != 6:
                    print(f"Ошибка в строке {line_num}: должно быть 6 полей")
                    continue
                
                try:
                    brand, model, year_str, body_type, mileage_str, price_str = parts
                    cars.append({
                        'brand': brand,
                        'model': model,
                        'year': int(year_str),
                        'body_type': body_type,
                        'mileage': int(mileage_str),
                        'price': float(price_str)
                    })
                except ValueError:
                    print(f"Ошибка в строке {line_num}: неверный тип данных")
                    continue
        
        if not cars:
            print("Файл пуст или не содержит валидных данных")
            return None
        
        print(f"Загружено {len(cars)} автомобилей")
        return cars
        
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден! Будет создан новый при сохранении.")
        return []  # Возвращаем пустой список вместо None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []


def write_report(cars, title, filename):
    """Запись отчета в файл."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{'='*80}\n{title}\n{'='*80}\n")
            
            if not cars:
                file.write("Нет автомобилей\n")
                return True
            
            for i, car in enumerate(cars, 1):
                file.write(f"{i:3}. {car['brand']:10} {car['model']:12} "
                          f"{car['year']:6} {car['body_type']:12} "
                          f"{car['mileage']:8} km ${car['price']:10.0f}\n")
            
            file.write(f"\nВсего: {len(cars)} автомобилей\n")
        print(f"Отчет сохранен в '{filename}'")
        return True
    except Exception as e:
        print(f"Ошибка записи: {e}")
        return False
