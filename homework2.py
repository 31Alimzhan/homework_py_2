# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр
'''
def summator(a):                                     # функция суммирования
    if a<1 : a=a*100000                              # !!! Костылек если а меньше 1 то умножаем на большое число чтобы сработал алгоритм
    sum = 0                                          # обозначаем переменную sum 
    while (a!=0):                                    # до тех пор пока а не равен нулю делаем
        p = a % 10                                   # отсекаем последнюю цифру и присваиваем p
        sum = sum + p                                # суммируем 
        a = a // 10                                  # целочисленное деление отсекаем последнюю цуифру 
    return sum                                       # возвращаем sum

a = float(input("Введите число "))                   # запрашиваем ввести число
sum = summator(a)                                    # вызываем функцию
print(sum)                                           # печатаем результат
'''

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N

def factorial(a):                                     # функция подсчета числа факториал
    fact = a                                          # !!! сразу присваиваем последнее значение числу так как в цикле for последнее значение не используется
    for i in range (1,a):                             # задаем цикл
        fact = fact * i                               # число умножаем на иттерационную переменную
    return fact                                       # возвращаем результат

a = int(input("Введите число "))                      # запрашиваем ввод числа
factor = factorial(a)                                 # вызываем функцию факториал
print(factor)                                         # печатаеам

