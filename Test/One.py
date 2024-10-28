# Целое число n называется совершенным, если сумма всех его собственных
# делителей равна самому числу n. Например, 28 – это совершенное число,
# поскольку его собственными делителями являются 1, 2, 4, 7 и 14, а 1 + 2 + 4 + 7 + 14 = 28.
# Напишите функцию для определения того, является ли заданное число
# совершенным. Функция будет принимать на вход единственный параметр и возвращать True, если он представляет собой совершенное число,
# и False – если нет. Разработайте небольшую программу, которая будет
# использовать функцию для идентификации и вывода на экран всех совершенных чисел в диапазоне от 1 до 10 000.
#
number = int(input('Enter a num... '))

def unuque_number(number):
    summ = 0
    i = 1
    j = 1
    while i <= number:
        while j < i:
            if i % j == 0:
                summ += j
            j = j + 1
        if summ == i:
            print("True ==================================================>")
            summ = 0
            j = 1
        else:
            print("false")
            summ = 0
            j = 1
        i = i + 1
