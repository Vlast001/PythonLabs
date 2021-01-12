# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке

str_list = ["Some string\n", "Some beautiful string\n", "VERY strange math expression\n"]

with open("test_2.txt", "a") as file_obj:
    file_obj.writelines(str_list)

with open("test_2.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split(' '))
        print(f"{words} words in line")
    print(f"Total string count is {lines}")
