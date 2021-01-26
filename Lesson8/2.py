"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class MyDivisionByZeroException(Exception):
    def __int__(self, text):
        self.text = text


try:
    a = float(input("Input divider"))
    b = float(input("Input denominator"))
    if b == 0:
        raise MyDivisionByZeroException("Деление на ноль, иди в школу!")
    c = a / b
except ValueError:
    print("Error type of value!")
except MyDivisionByZeroException as dbz:
    print(dbz)
