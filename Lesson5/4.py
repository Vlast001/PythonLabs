"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыри'}
result = []

try:
    with open("test_4_input.txt", 'r', encoding='utf8') as file_obj:
        for i in file_obj:
            i = i.split(' ', 1)
            result.append(translator[i[0]] + '  ' + i[1])
        print(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")

try:
    with open("test_4_output.txt", "w", encoding='utf8') as file_input:
        file_input.writelines(result)
except IOError:
    print("Произошла ошибка ввода-вывода!")
