# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества:"))
m = int(input("Введите количество элементов второго множества:"))
my_list_1=[]
for i in range(n):
    num = int(input("Введите элемент первого множества: "))
    my_list_1.append(num)
my_list2 = [int(input("Введите элемент второго множества: ")) for i in range(m)]
print(my_list_1)
print(my_list2)
new_list = set(my_list_1).intersection(set(my_list2))
print(new_list)