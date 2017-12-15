"""
Имеется файл с данными по успеваемости абитуриентов.
 Он представляет из себя набор строк, где в каждой строке записана следующая информация:

Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку

Поля внутри строки разделены точкой с запятой, оценки — целые числа.

Напишите программу, которая считывает файл с подобной структурой и для
 каждого абитуриента выводит его среднюю оценку по этим трём предметам на
 отдельной строке, соответствующей этому абитуриенту.

Также в конце файла, на отдельной строке, через пробел запишите средние
баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать
метод split следующим образом:

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']
Sample Input:

Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output:

85.0
94.0
71.666666667
81.0 84.0 85.666666667
"""




#first solution
with open('file.txt') as file:
    lst = [x.strip().split(';') for x in file]
    lst = [x[1:]for x in lst]
    lst = [[float(i[j]) for j in range(3)] for i in lst]
    lst2 = [[float(x[j]) for x in lst] for j in range(3)]
    sum_per_marks = [round((sum(x) / len(x)), 9) for x in lst2]
    sum_per_person = [round(sum(x) / len(lst2), 9) for x in lst]

with open('dataset_3363_4.txt', "w") as file:
    [file.write(str(x) + '\n') for x in sum_per_person]
    [file.write(str(x) + ' ') for x in sum_per_marks]


#second solution:
st = [x.split(';') for x in open('fl.txt').readlines()]
print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
