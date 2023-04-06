# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input("Введите количество элементов: "))

import random
my_list = [ random.randint(1,10) for i in range(N+1)]
print(my_list)
X = int(input("Введите число: "))
if X > N:
   print(f"число {X} больше чем количество элементов, введите другое число")
else:

    new_list = [i for i in my_list if  i/X >= 1] 
    print(new_list)
    min = ""
    for i in range(len(new_list)):
     if i < i+1:
         min = new_list[i]


    print(min)
