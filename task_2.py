# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# n = int (input ("Введите число: "))
# import random
# rand_list=[]
# for i in range(n):
# 	rand_list.append(random.randint(1,10))
# print(rand_list)
# print(f"Cумма чисел, стоящих на нечётных позициях: {sum(rand_list[1::2])}")

n = int (input ("Введите число: "))
import random
rand_list=[]
for i in range(n):
	rand_list.append(random.randint(1,10))
sum_odd = []
sum_odd = sum(rand_list[item] for item in range(1, len(rand_list), 2))
odd_el = str([rand_list[item] for item in range(1, len(rand_list), 2)]).strip('[]')
print(f'{rand_list}\nCумма чисел, стоящих на нечётных позициях: {sum_odd}')