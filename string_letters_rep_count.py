"""
Узнав, что ДНК не является случайной строкой, только что поступившие
 в Институт биоинформатики студенты группы информатиков предложили
  использовать алгоритм сжатия, который сжимает повторяющиеся
   символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной
 строки заменяются на этот символ и количество
  его повторений в этой позиции строки.

Напишите программу, которая считывает строку,
 кодирует её предложенным алгоритмом и выводит
  закодированную последовательность на стандартный
вывод. Кодирование должно учитывать регистр символов.
"""

s = "aaaabbсaa"
output = ""
count = 1
е = len(s)
for i in range(0,len(s)-2):
    for j in range(1,len(s)-1):
        if s[i] == s[j]:
            count +=1
        else:
            output = output + s[i] + str(count)
            count = 1
        i+=1
        j+=1