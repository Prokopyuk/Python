"""
Недавно мы считали для каждого слова количество его
 вхождений в строку. Но на все слова может быть не
 так интересно смотреть, как, например, на наиболее
 часто используемые.

Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит
 самое частое слово в этом тексте и через пробел то,
  сколько раз оно встретилось. Если таких слов несколько,
   вывести лексикографически первое (можно использовать
   оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC
Sample Output:
abc 3
"""
max_val = 0
with open("input_file.txt") as file:
    lst = [x.strip() for x in file]
    a = " ".join(lst)
    b = set([x for x in a.lower().split()])
    d = {key: a.lower().split().count(key) for key in b}
    max_val =  (max(zip(d.keys(),d.values())))

with open('output_file.txt', "w") as file:
    file.write(str(max_val))


