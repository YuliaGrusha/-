# main.py - главная программа
from file_operations import read_cars_from_file, write_report
from reports import create_report1_all_cars, create_report2_by_brand, create_report3_by_price_range
from data_operations import add_car, remove_car, edit_car, save_data_to_file, show_all_cars


def display_main_menu():
    """Отображение главного меню программы."""
    print("\n" + "="*80)
    print("ПРОГРАММА 'АВТОДИЛЕР'")
    print("="*80)
    print("1. Работа с данными (добавить/удалить/редактировать)")
    print("2. Создание отчетов")
    print("3. Показать все автомобили")
    print("4. Сохранить данные в файл")
    print("5. Выход")
    print("="*80)


def display_data_menu():
    """Меню работы с данными."""
    print("\n" + "="*80)
    print("РАБОТА С ДАННЫМИ")
    print("="*80)
    print("1. Добавить автомобиль")
    print("2. Удалить автомобиль")
    print("3. Редактировать автомобиль")
    print("4. Вернуться в главное меню")
    print("="*80)


def display_reports_menu():
    """Меню создания отчетов."""
    print("\n" + "="*80)
    print("СОЗДАНИЕ ОТЧЕТОВ")
    print("="*80)
    print("1. Все автомобили (год ↓ + цена ↑)")
    print("2. Автомобили определенной марки")
    print("3. Автомобили в диапазоне цен")
    print("4. Вернуться в главное меню")
    print("="*80)


def handle_data_operations(cars_data):
    """Обработка операций с данными."""
    while True:
        display_data_menu()
        choice = input("\nВыбор: ").strip()
        
        if choice == '1':
            add_car(cars_data)
        elif choice == '2':
            remove_car(cars_data)
        elif choice == '3':
            edit_car(cars_data)
        elif choice == '4':
            break
        else:
            print("Неверный выбор")
        
        input("\nНажмите Enter для продолжения...")


def handle_reports_operations(cars_data):
    """Обработка создания отчетов."""
    while True:
        display_reports_menu()
        choice = input("\nВыбор: ").strip()
        
        if choice == '1':
            # Отчет 1
            sorted_cars = create_report1_all_cars(cars_data)
            if sorted_cars:
                # Сохраняем в файл
                write_report(sorted_cars,
                           "ОТЧЕТ 1: Все автомобили (сортировка: год выпуска ↓ + цена ↑)",
                           "отчет1.txt")
        
        elif choice == '2':
            # Отчет 2
            result = create_report2_by_brand(cars_data)
            if result:
                sorted_cars, brand = result
                # Сохраняем в файл
                write_report(sorted_cars,
                           f"ОТЧЕТ 2: Автомобили марки {brand} (сортировка: тип кузова ↑ + год ↓ + цена ↑)",
                           "отчет2.txt")
        
        elif choice == '3':
            # Отчет 3
            result = create_report3_by_price_range(cars_data)
            if result:
                sorted_cars, min_p, max_p = result
                # Сохраняем в файл
                write_report(sorted_cars,
                           f"ОТЧЕТ 3: Автомобили в диапазоне цен ${min_p:.0f}-${max_p:.0f} (сортировка: цена ↑ + пробег ↑)",
                           "отчет3.txt")
        
        elif choice == '4':
            break
        
        else:
            print("Неверный выбор")
        
        input("\nНажмите Enter для продолжения...")


def main():
    """Основная функция программы."""
    print("Программа 'Автодилер'")
    print("="*80)
    
    # Загрузка данных
    cars_data = read_cars_from_file('cars.txt')
    if cars_data is None:
        cars_data = []  # Создаем пустой список, если файла нет
    
    # Главный цикл программы
    while True:
        display_main_menu()
        choice = input("\nВыбор: ").strip()
        
        if choice == '1':
            handle_data_operations(cars_data)
        
        elif choice == '2':
            handle_reports_operations(cars_data)
        
        elif choice == '3':
            show_all_cars(cars_data)
            input("\nНажмите Enter для продолжения...")
        
        elif choice == '4':
            save_data_to_file(cars_data, 'cars.txt')
            input("\nНажмите Enter для продолжения...")
        
        elif choice == '5':
            # Предлагаем сохранить перед выходом
            save_choice = input("\nСохранить изменения перед выходом? (да/нет): ").lower()
            if save_choice in ['да', 'д', 'yes', 'y']:
                save_data_to_file(cars_data, 'cars.txt')
            print("\nВыход из программы...")
            break
        
        else:
            print("Неверный выбор")
            input("\nНажмите Enter для продолжения...")


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()


