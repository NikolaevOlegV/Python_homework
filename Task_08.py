# Задача 8
# Требуется определить, можно ли от шоколадки 
# размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите в 1 шоколаде количество долек: "))
m = int(input("Введите во 2 шоколаде количество долек: "))

k = int(input("Введите количество долек, которое хотите получить: "))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Да')
else:
    print('Нет')