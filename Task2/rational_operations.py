# import menu
import logger

def start(a, b, op):

    oper = {
  '+': lambda x, y: float(x) + float(y),
  '-': lambda x, y: float(x) - float(y),
  '*': lambda x, y: float(x) * float(y),
  '/': lambda x, y: float(x) / float(y)
    }
    
    logger.logging.info(f"Entered number {a} and {b}")
        
    if op == '/' and b == 0:
        return "На ноль делить нельзя!"
        
    else:
        return oper[op](a, b)





    # op = menu.menu_op()
    # logger.logging.info(f"Entered number {op}")
    # if op > 4 or op < 1:
    #     print("Вы ввели чушь!")
    # else:
        # a, b = map(float, input("\nВведите значение через пробел: ").split())
        # logger.logging.info(f"Entered number {a} and {b}")
        # if op == 4 and b == 0:
        #     print("Делить на ноль нельзя!!!")
        
        # else:
        #     print(f"Результат вычисления {a} и {b} равняется: {oper[op](a, b)}")