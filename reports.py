# reports.py - функции для создания отчетов
from sort import bin_insertion_sort

def create_report1_all_cars(cars_data):
    """Отчет 1: Все автомобили (год ↓ + цена ↑)"""
    sorted_cars = bin_insertion_sort(
        [c.copy() for c in cars_data],
        [(lambda x: x['year'], True), (lambda x: x['price'], False)]
    )
    
    # Вывод на консоль
    print_report_to_console(sorted_cars, 
                          "ОТЧЕТ 1: Все автомобили (сортировка: год выпуска ↓ + цена ↑)")
    
    return sorted_cars


def create_report2_by_brand(cars_data):
    """Отчет 2: Автомобили определенной марки"""
    brand = input("Марка: ").strip()
    filtered = [car for car in cars_data if car['brand'].lower() == brand.lower()]
    
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
    
    # Вывод на консоль
    print_report_to_console(sorted_cars,
                          f"ОТЧЕТ 2: Автомобили марки {brand} (сортировка: тип кузова ↑ + год ↓ + цена ↑)")
    
    return sorted_cars, brand


def create_report3_by_price_range(cars_data):
    """Отчет 3: Автомобили в диапазоне цен"""
    try:
        min_p = float(input("Минимальная цена: "))
        max_p = float(input("Максимальная цена: "))
        
        if min_p > max_p:
            print("Ошибка: минимальная цена больше максимальной")
            return None
        
        filtered = [car for car in cars_data if min_p <= car['price'] <= max_p]
        
        if not filtered:
            print(f"В диапазоне ${min_p:.0f}-${max_p:.0f} не найдено")
            return None
        
        sorted_cars = bin_insertion_sort(
            [c.copy() for c in filtered],
            [(lambda x: x['price'], False), (lambda x: x['mileage'], False)]
        )
        
        print(f"Найдено {len(filtered)} автомобилей в диапазоне ${min_p:.0f}-${max_p:.0f}")
        
        # Вывод на консоль
        print_report_to_console(sorted_cars,
                              f"ОТЧЕТ 3: Автомобили в диапазоне цен ${min_p:.0f}-${max_p:.0f} (сортировка: цена ↑ + пробег ↑)")
        
        return sorted_cars, min_p, max_p
        
    except ValueError:
        print("Ошибка: введите числа")
        return None


def print_report_to_console(cars, title, limit=10):
    """Вывод отчета на консоль"""
    print(f"\n{'='*80}")
    print(f"{title}")
    print(f"{'='*80}")
    
    if not cars:
        print("Нет автомобилей, соответствующих критериям")
        return
    
    print("№   Марка       Модель         Год   Тип кузова      Пробег     Цена")
    print("-" * 80)
    
    # Ограничиваем вывод для удобства просмотра
    display_cars = cars[::]
    for i, car in enumerate(display_cars, 1):
        print(f"{i:3}. {car['brand']:10} {car['model']:12} "
              f"{car['year']:6} {car['body_type']:12} "
              f"{car['mileage']:8} km ${car['price']:10.0f}")

    
    print(f"\nВсего автомобилей: {len(cars)}")
    print("=" * 80)
