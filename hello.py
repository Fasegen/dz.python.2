# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
x = int(input())
y = []
for i in range(1, x+1):
    y.append(f'{i}: ' + str(3*i+1))

print(y)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
x = []
N = int(input())
c = 1
for i in range(1,N+1):
    c = c * i
    x.append(c)
print(x)

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
x = float(input())
sum = 0
for i in str(x):
        if i != ".":
            sum += int(i)
print(sum)

# def sumNums(num):
#     sum = 0
#     for i in str(num):
#         if i != ".":
#             sum += int(i)
#     return sum

# print(f"Сумма цифр = {sumNums(4.234)}")



# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

y = [5, 1, 2, 7, 3, 2]
x = [1, 2, 3, 2, 0]
c = []
for i in y:
    for j in x:
        if j == i:
            c.append(j)
            x[j-1] = "haha"
            break
c.sort()         
print(c)

# Задача с Практического занятия
A = input().split()
B = input().split()
count = 0
for i in A:
    for k in B:
        if i == k:
            count += 1
print(count)