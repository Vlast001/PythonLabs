
"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
'''Вариант с генератором'''
my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

# Вариант с циклом
i = 0
new= []
for el in my_list:
    if el > my_list[i-1]:
        new.append(el)
    i+=1
print(new)
