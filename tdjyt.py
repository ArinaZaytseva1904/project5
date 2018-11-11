"""
Написать программу, которая считывает данные из файла spisok.txt и передает данные в osnova.txt.
"""

i = 0
file_1 = open('spisok.txt', 'r', encoding='utf-8')
file_2 = open('osnova.txt', 'w', encoding='utf-8')
for line in file_1.readlines():
    i += 1
    if i < 10:
        a = line[i]
        a = a.upper()
        print(a)
        file_2.write(line.upper())
file_1.close()
file_2.close()
i = 0
file_1 = open('spisok.txt', 'r', encoding='utf-8')
file_2 = open('osnova.txt', 'w', encoding='utf-8')
for line in file_1.readlines():
    i += 1
    if i < 10:
        a = line[i]
        a = a.lower()
        print(a)
        file_2.write(line.lower())
    else:
        break
file_1.close()
file_2.close()
