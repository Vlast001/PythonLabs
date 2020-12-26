"""
Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def div(arg1, arg2):
    try:
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Division by zero!"

    return res


a = int(input("Input dividend: "))
b = int(input("Input divider: "))
print(f'Division result:  {div(a, b)}')
