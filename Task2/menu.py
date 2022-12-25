# import operations
# import logger

# def menu():
    
#     while True:
#         print("\n1. Произвести вычисления")
#         print("2. Вывести log")
#         print("3. Закрыть программу\n")

#         try:
#             number_menu = int(input('Выберите пункт меню: '))
#         except ValueError:
#             print("Вы ввели чушь!")
#             break

#         if number_menu == 1:
#             logger.logging.info(f"Entered number {number_menu}")
#             print("\n1. Вычисление рациональных чисел")
#             print("2. Вычисление комплексных чисел\n")
            
#             try:
#                 operations.op(int(input('Выберите пункт меню: ')))
#             except ValueError:
#                 print("Вы ввели чушь!")
#                 break

#         elif number_menu == 2:
#             logger.logging.info(f"Entered number {number_menu}")
#             logger.read_file()

#         elif number_menu == 3:
#             logger.logging.info(f"Entered number {number_menu}")
#             print("Спасибо, что воспользовались нашей программой.")
#             break

#         else:
#             logger.logging.info(f"Entered number {number_menu}")
#             print("Такого пункта меню нету!")
                
# def menu_op():
#     print("\nВыберите операцию, которую нужно произвести с числами.")
#     print("1. Сложение")
#     print("2. Разность")
#     print("3. Произведение")
#     print("4. Деление\n")

#     return int(input("Выберите операцию: "))