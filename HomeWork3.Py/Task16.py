# ;  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# ;  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# ;  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# ; *Пример:*

# ; 5
# ;     1 2 3 4 5
# ;     3
# ;     -> 1

N = int(input("Введите количество элементов: "))
import random
my_list = [ random.randint(1,10) for i in range(N+1)]
print(my_list)
numb = int(input("Введите число: "))
count=0
for i in my_list:
    if i == numb:
        count=count+1
    #print(i)
print(count)