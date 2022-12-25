# import menu
import logger

def start(a, b):

    oper = {
  1: lambda x, y: x + y,
  2: lambda x, y: x - y,
  3: lambda x, y: x * y,
  4: lambda x, y: x / y
    }

    # # op = menu.menu_op()
    # logger.logging.info(f"Entered number {op}")

    if op > 4 or op < 1:
        print("Вы ввели чушь!")
    else:
        a = complex(input("Введите комплексное число A: ").replace(' ', ''))
        b = complex(input("Введите комплексное число B: ").replace(' ', ''))
        logger.logging.info(f"Entered number {a} and {b}")

        print(f"Результат вычисления {a} и {b} равняется: {oper[op](a, b)}")
