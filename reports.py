def create_report1_all_cars(cars_data):
    """Отчет 1: Все автомобили (год ↓ + цена ↑)"""
    from sort import bin_insertion_sort
    
    sorted_cars = bin_insertion_sort(
        [c.copy() for c in cars_data],
        [(lambda x: x['year'], True), (lambda x: x['price'], False)]
    )
    
    # Краткий вывод на экран
    print(f"\nПервые 5 из {len(sorted_cars)} автомобилей:")
    for i in range(min(5, len(sorted_cars))):
        c = sorted_cars[i]
        print(f"{i+1}. {c['brand']} {c['model']} ({c['year']}) - ${c['price']:.0f}")
    
    return sorted_cars


def create_report2_by_brand(cars_data):
    """Отчет 2: Автомобили определенной марки"""
    from sort import bin_insertion_sort
    
    brand = input("Марка: ").strip()
    filtered = [c for c in cars_data if c['brand'].lower() == brand.lower()]
    
    if not filtered:
        print(f"Марка '{brand}' не найдена")
        return None
    
    sorted_cars = bin_insertion_sort(
        [c.copy() for c in filtered],
        [
            (lambda x: x['body_type'], False),
            (lambda x: x['year'], True),
            (lambda x: x['price'], False)
        ]
    )
    
    print(f"Найдено {len(filtered)} автомобилей марки {brand}")
    return sorted_cars, brand


def create_report3_by_price_range(cars_data):
    """Отчет 3: Автомобили в диапазоне цен"""
    from sort import bin_insertion_sort
    
    try:
        min_p = float(input("Минимальная цена: "))
        max_p = float(input("Максимальная цена: "))
        
        if min_p > max_p:
            print("Ошибка: минимальная цена больше максимальной")
            return None
        
        filtered = [c for c in cars_data if min_p <= c['price'] <= max_p]
        
        if not filtered:
            print(f"В диапазоне ${min_p:.0f}-${max_p:.0f} не найдено")
            return None
        
        sorted_cars = bin_insertion_sort(
            [c.copy() for c in filtered],
            [(lambda x: x['price'], False), (lambda x: x['mileage'], False)]
        )
        
        print(f"Найдено {len(filtered)} автомобилей в диапазоне ${min_p:.0f}-${max_p:.0f}")
        return sorted_cars, min_p, max_p
        
    except ValueError:
        print("Ошибка: введите числа")
        return None