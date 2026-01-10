# data_operations.py - операции с данными автомобилей

def add_car(cars_data):
    """Добавление нового автомобиля."""
    print("\n" + "="*80)
    print("ДОБАВЛЕНИЕ НОВОГО АВТОМОБИЛЯ")
    print("="*80)
    
    while True:
        try:
            brand = input("Марка: ").strip()
            model = input("Модель: ").strip()
            year = int(input("Год выпуска: ").strip())
            body_type = input("Тип кузова: ").strip()
            mileage = int(input("Пробег (км): ").strip())
            price = float(input("Цена ($): ").strip())
        
            new_car = {
                'brand': brand,
                'model': model,
                'year': year,
                'body_type': body_type,
                'mileage': mileage,
                'price': price
            }
        
            cars_data.append(new_car)
            print(f"\nАвтомобиль {brand} {model} успешно добавлен!")
            break
        
        except ValueError:
            print("Ошибка: неверный формат данных")
            continue


def remove_car(cars_data):
    """Удаление автомобиля."""
    print("\n" + "="*80)
    print("УДАЛЕНИЕ АВТОМОБИЛЯ")
    print("="*80)
    
    if not cars_data:
        print("Список автомобилей пуст")
        return False
    
    # Показываем все автомобили с номерами
    print("Список автомобилей:")
    for i, car in enumerate(cars_data, 1):
        print(f"{i:3}. {car['brand']} {car['model']} ({car['year']}) - ${car['price']:.0f}")
    
    try:
        car_num = int(input("\nНомер автомобиля для удаления (0 - отмена): "))
        
        if car_num == 0:
            print("Удаление отменено")
            return False
        
        if 1 <= car_num <= len(cars_data):
            removed_car = cars_data.pop(car_num - 1)
            print(f"\nАвтомобиль {removed_car['brand']} {removed_car['model']} удален!")
            return True
        else:
            print("Неверный номер автомобиля")
            return False
            
    except ValueError:
        print("Ошибка: введите число")
        return False


def edit_car(cars_data):
    """Редактирование автомобиля."""
    print("\n" + "="*80)
    print("РЕДАКТИРОВАНИЕ АВТОМОБИЛЯ")
    print("="*80)
    
    if not cars_data:
        print("Список автомобилей пуст")
        return False
    
    # Показываем все автомобили с номерами
    print("Список автомобилей:")
    for i, car in enumerate(cars_data, 1):
        print(f"{i:3}. {car['brand']} {car['model']} ({car['year']}) - ${car['price']:.0f}")
    
    try:
        car_num = int(input("\nНомер автомобиля для редактирования (0 - отмена): "))
        
        if car_num == 0:
            print("Редактирование отменено")
            return False
        
        if not (1 <= car_num <= len(cars_data)):
            print("Неверный номер автомобиля")
            return False
        
        car_to_edit = cars_data[car_num - 1]
        print(f"\nРедактирование: {car_to_edit['brand']} {car_to_edit['model']}")
        print("(Оставьте поле пустым, чтобы не изменять значение)")
        
        # Редактирование полей
        new_brand = input(f"Марка [{car_to_edit['brand']}]: ").strip()
        if new_brand:
            car_to_edit['brand'] = new_brand
        
        new_model = input(f"Модель [{car_to_edit['model']}]: ").strip()
        if new_model:
            car_to_edit['model'] = new_model
        
        new_year = input(f"Год [{car_to_edit['year']}]: ").strip()
        if new_year:
            try:
                car_to_edit['year'] = int(new_year)
            except ValueError:
                print("Ошибка: год должен быть числом")
        
        new_body_type = input(f"Тип кузова [{car_to_edit['body_type']}]: ").strip()
        if new_body_type:
            car_to_edit['body_type'] = new_body_type
        
        new_mileage = input(f"Пробег [{car_to_edit['mileage']}]: ").strip()
        if new_mileage:
            try:
                car_to_edit['mileage'] = int(new_mileage)
            except ValueError:
                print("Ошибка: пробег должен быть числом")
        
        new_price = input(f"Цена [{car_to_edit['price']}]: ").strip()
        if new_price:
            try:
                car_to_edit['price'] = float(new_price)
            except ValueError:
                print("Ошибка: цена должна быть числом")
        
        print(f"\nАвтомобиль обновлен!")
        return True
        
    except ValueError:
        print("Ошибка: введите число")
        return False


def save_data_to_file(cars_data, filename):
    """Сохранение данных в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        for car in cars_data:
            line = f"{car['brand']},{car['model']},{car['year']},{car['body_type']},{car['mileage']},{car['price']}\n"
            file.write(line)
    print(f"Данные сохранены в файл '{filename}'")
    return True


def show_all_cars(cars_data):
    """Показать все автомобили."""
    print("\n" + "="*80)
    print("ВСЕ АВТОМОБИЛИ В БАЗЕ")
    print("="*80)
    
    if not cars_data:
        print("Список автомобилей пуст")
        return
    
    for i, car in enumerate(cars_data, 1):
        print(f"{i:3}. {car['brand']:10} {car['model']:12} "
              f"{car['year']:6} {car['body_type']:12} "
              f"{car['mileage']:8} km ${car['price']:10.0f}")
    
    print(f"\nВсего: {len(cars_data)} автомобилей")
