#  В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.


n = int(input("Введите количесвто кустов: "))
# x = int(input("Введите количесвто ягод: "))
my_list = [int(input("Введите количесвто ягод: ")) for i in range(n)]
print(my_list)

max1=0
my_list=my_list+my_list[:2]
print(my_list)
for i in range(n):
    
    max1 = max( max1, my_list[i] + my_list[i+1] + my_list[i+2] )
    
        
    print(max1)
    print(my_list)


print(f"максимальное число ягод будет равно: {max1}")



