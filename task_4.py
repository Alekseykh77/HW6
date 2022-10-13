# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Число должно быть integer ")
#     return number

# def mult(num):
#     if num == 1:
#         return 1
#     else:
#         return num * mult(num - 1)

# num = InputNumbers("Введите число: ")

# list = []
# for e in range(1, num + 1):
#     list.append(mult(e))

# print(f"Произведения чисел от 1 до {num}:  {list}")

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number
num = InputNumbers("Введите число: ") 
rand_list=[i for i in range(1,num+1)]

def mult(num):
    if num == 1:
        return 1
    else:
        return num * mult(num - 1)
       
new_list = list(map(mult, rand_list))
# new_list = str(tuple(new_list))	меняет кваодратные скобки на круглые
print(f"N = {num}, тогда произведения от 1 до N {new_list}")