"""
5.
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
"""
try:
    with open('file_5.txt', 'w') as file_obj:
        line = "2 2 2 2 2 2"
        file_obj.writelines(line)
    with open('file_5.txt', "r") as file_obj:
        read_line = file_obj.readline()
        # print(read_line)
        my_numb = read_line.split()
        print(sum(map(int, my_numb)))
except IOError:
    print("Ошибка в файле")
except ValueError:
    print("Неправильно набран номер. Ошибка ввода-вывода")