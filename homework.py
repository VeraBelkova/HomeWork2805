# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input("Введите колич монеток: "))
# i = 0
# count1 = 0
# count2 = 0
# while i<= n:
#     m = int(input("Введите 1 - орел, 2 - решка: "))
#     if m == 1:
#       count1 += m
#     else:
#        m = 2
#        count2 += m
#     i += 1
# if count1 > count2:
#    print(f"Минимальное число, которые нужно перевернуть - {count2}")
# else:
#    print(f"Минимальное число, которые нужно перевернуть - {count1}") 


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# sum = int(input("Введите сумму чисел x и y: "))
# umn = int(input("Введите произведение чисел x и y: "))
# for x in range(sum):
#     for y in range(umn):
#        if sum == x + y and umn == x * y:
#           print(x, y)


#  Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N: "))
i = 0
while 2** i <= n:
    print(2**i)
    i += 1