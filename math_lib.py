"""
Напишите программу, которая подключает модуль math и,
 используя значение числа ππ из этого модуля, находит
 для переданного ей на стандартный ввод радиуса круга
  периметр этого круга и выводит его на стандартный вывод.

Sample Input:
10.0
Sample Output:
62.83185307179586
"""

from math import pi

def get_circle_perimeter():
    print (2*pi*float(input()))

get_circle_perimeter()