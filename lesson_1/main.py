# '''
# Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните
# в переменные, выведите на экран.
# '''
#
# a = 12
# b = 24
# print("Переменные a и b - ", a, b)
# str1 = input("Введите первую строку ")
# str2 = input("Введите вторую строку ")
# num1 = int(input("Введите первое число "))
# num2 = int(input("Введите второе число "))
# print(f"Введеные значения - {str1} {str2} {num1} {num2}")
#
# '''
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# '''
#
# time = int(input("Введите время в секундах "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")
#
# '''
# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369
# '''
#
# n = int(input("Введите число - "))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print(f"Сумма чисел n + nn + nnn - {total}")
#
# '''
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# '''
# n = abs(int(input("Введите целое положительное число ")))
# max_int = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max_int:
#         max_int = n % 10
#     if n > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max_int)
#         break
# '''
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или
# убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.
# '''
#
# profit = float(input("Введите выручку фирмы "))
# costs = float(input("Введите издержки фирмы "))
# if profit > costs:
#     print(f"Фирма работает с прибылью. Рентабельность выручки составила {profit / costs:.2f}")
#     workers = int(input("Введите количество сотрудников фирмы "))
#     print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
# elif profit == costs:
#     print("Фирма работает в ноль")
# else:
#     print("Фирма работает в убыток")
#
# '''
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего.
# Требуется определить номер дня, на который общий
# результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
# '''

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    a = a + 0.1 * a
    result_days += 1
    result_km += a
print(f"Вы достигнете требуемых показателей на {result_days} день")