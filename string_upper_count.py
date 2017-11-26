"""
GC-состав является важной характеристикой геномных последовательностей и
определяется как процентное соотношение суммы всех гуанинов и цитозинов
 к общему числу нуклеиновых оснований в геномной последовательности.

Напишите программу, которая вычисляет процентное содержание символов
 G (гуанин) и C (цитозин) в введенной строке (программа не должна
 зависеть от регистра вводимых символов).

Например, в строке "acggtgttat" процентное содержание символов
G и C равно 410⋅100=40.0410⋅100=40.0, где 4 -- это количество
 символов G и C,  а 10 -- это длина строки..
"""
s,result= input(), 0
result = (s.upper().count("G") + s.upper().count("C")) / len(s) * 100
print(result)