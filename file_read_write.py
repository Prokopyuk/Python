"""
Напишите программу, которая считывает из файла строку,
 соответствующую тексту, сжатому с помощью кодирования
  повторов, и производит обратную операцию, получая
  исходный текст.

Запишите полученный текст в файл и прикрепите его,
 как ответ на это задание.

В исходном тексте не встречаются цифры, так что код
 однозначно интерпретируем.
"""
import re
with open ("dataset_3363_2.txt", "a")as f :
    f.write("a2a10b1")


s1 = ""
s2 = ""
lst = []

with open("dataset_3363_2.txt","r") as input:
    s1 = input.readline().strip()

lst = re.split('(\d*)', s1)

with open('dataset_3363_2.txt', "w") as output:
    for i in range(0, len(lst)-2, 2):
        s2+= lst[i] * int(lst[i+1])
    output.write(s2)
