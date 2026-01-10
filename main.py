from file_operations import read_cars_from_file, write_report
from reports import create_report1_all_cars, create_report2_by_brand, create_report3_by_price_range


def display_menu():
    """Отображение меню программы."""
    print("\n" + "="*80)
    print("ПРОГРАММА 'АВТОДИЛЕР'")
    print("="*80)
    print("1. Все автомобили (год ↓ + цена ↑)")
    print("2. Автомобили определенной марки")
    print("3. Автомобили в диапазоне цен")
    print("4. Выход")
    print("="*80)


def main():
    """Основная функция программы."""
    print("Программа 'Автодилер'")
    print("="*80)
    
    # Загрузка данных
    cars_data = read_cars_from_file('cars.txt')
    if not cars_data:
        input("\nНажмите Enter для выхода...")
        return
    
    # Главный цикл программы
    while True:
        display_menu()
        choice = input("\nВыбор: ").strip()
        
        if choice == '1':
            # Отчет 1
            sorted_cars = create_report1_all_cars(cars_data)
            if sorted_cars:
                write_report(sorted_cars,
                           "ОТЧЕТ 1: Все автомобили (год выпуска ↓ + цена ↑)",
                           "отчет1.txt")
        
        elif choice == '2':
            # Отчет 2
            result = create_report2_by_brand(cars_data)
            if result:
                sorted_cars, brand = result
                write_report(sorted_cars,
                           f"ОТЧЕТ 2: Автомобили марки {brand} (тип кузова ↑ + год ↓ + цена ↑)",
                           "отчет2.txt")
        
        elif choice == '3':
            # Отчет 3
            result = create_report3_by_price_range(cars_data)
            if result:
                sorted_cars, min_p, max_p = result
                write_report(sorted_cars,
                           f"ОТЧЕТ 3: Автомобили в диапазоне цен ${min_p:.0f}-${max_p:.0f} (цена ↑ + пробег ↑)",
                           "отчет3.txt")
        
        elif choice == '4':
            print("\nВыход из программы...")
            break
        
        else:
            print("Неверный выбор. Введите число от 1 до 4.")
        
        input("\nНажмите Enter для продолжения...")
if __name__ == '__main__':
    main()