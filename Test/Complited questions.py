import random   # импортирую модуль для генерации случайного числа

'''Возвращает второе поп величине значение'''
def second_beginning(n):
    '''Переменные для храниения значений'''
    num_max = max(nums) # максимальное
    num_min = min(nums) # минимальное
    num_half = 0 # искомое значение
    print(f'Макс. значение: {num_max}, мин. значение: {num_min}')
    # прохожу по списку циклом
    for i in nums:
        if i >= num_min and i < num_max: # Проверяю условие
            num_min = i
            num_half = i
    return f"Искомое значение - второе по величине в списке: {num_half}." # возвращаю значение ввиде строки
num_2 = second_beginning(nums)
print(num_2)

'''Возвращает сумму нечетных чисел из списка'''
def odd_numbers_summ(nu):
    summ = 0
    for i in nu:
        if i % 2 != 0:
            summ += i
    return summ

'''Возвращает сумму нечетных чисел из списка. Генерирует список.'''
def Odd_Num_generation(rng):
    num_l = [value for value in range(1, rng, 2)]
    summ = 0
    for num in num_l:
        summ += num
    return f'Сумма всех нечетных чисел: {summ}.'

'''Вывести общие элементы для каждого списка'''
# создаю множество, передаю аргуметом сумму 2х списков
l = set(nums + nums_1)
print(l)

'''Получить первый и последний элемент списка.'''
print(f'Первый элемент списка: {nums[0]}, последний элемент списка: {nums[-1]}.')

'''Поиск цифры в натуральном числе'''
search_num = '8'    # переменная искомого числа
index = 0       # Номер позиции.
current_index = 1   # текущая позиция
natural_num = list(str(input('Enter a natural num...')))    # считываю с клавиатуры число, привожу его к типу: строка, конвертирую строку в список
for num in reversed(natural_num):
    if num == search_num:
        index = current_index
        if index >= 1:
            index = current_index
        current_index += 1
    elif num != search_num:
        current_index += 1
if index >= 1:
    print(index)
else:
    print('0')

'''Задача из лабораторной'''
natural_number = int(input('Enter a natural number...'))
question_number_k = int(input('Enter a second number...'))
question_number_b = int(input('Enter a trid number...'))
summ = 0    # Сумма первого натурального числа
nn_str = list(str(natural_number))  # список из первого числа
nuber_count = len(nn_str)   # Количество цифр в числе
for num in nn_str:
    summ += int(num)
if summ > question_number_k and summ % 2 == 0:
    print(f"Cумма цифр числа {natural_number} = {summ}, это больше чем число - {question_number_k}.")
if nuber_count % 2 == 0 and natural_number <= question_number_b:
    print(f'Кол-во цифр числа {natural_number} - число четное. Число {natural_number} не превышает число {question_number_b}')
else:
    print('Утверждения не верны!')

'''Задача из лабораторной -  найти все делители числа'''
num = int(input("Enter a number..."))
delitel = 1
del_List = []
while delitel <= num:
    if num % delitel == 0:
        del_List.append(delitel)
    delitel += 1
print(f"Все делители числа {num}: {del_List}.")

'''Дан массив, содержащий 15 элементов. Все положительные
элементы возвести в квадрат, а отрицательные умножить на 2. Вывести
исходный и полученный массив.'''

# Создаю массивы для хранения чисел
nums = []   # массив для начальных даннх
nums_new = []   # массив бля новых данных

i = 0
while i <= 14:
    rand = random.randint(-20, 20)  # генерирую число
    nums.append(rand)   # добавляю число в список
    i += 1

for j in nums:
    if j < 0:   # Проверяю условия добавляю полученное число в новый массив
        j =  j * 2
        nums_new.append(j)
    elif j > 0:
        j = j ** 2
        nums_new.append(j)
print(f"Входной массив: {nums}. Хранит {len(nums)} элементов.")
print(f"Массив с новыми данными: {nums_new}. Хранит {len(nums_new)} элементов.")

'''Выводит количество элементов болшее чем половина максимума'''
# Создаю массивы для хранения чисел
nums = []   # массив для начальных даннх
i = 0
while i <= 49:
    rand = random.randint(1, 150)  # генерирую число
    nums.append(rand)   # добавляю число в список
    i += 1
half_max = len(nums) / 2    # половина длины списка
count = 0   # количество элементов
for i in nums:
    if i > half_max:
        count += 1
print(f"Количество элементов, больших чем половина максимума: {count}.")
print(nums)

'''Найти произведение элементов массива вещественных чисел K(25),
расположенных после максимального по модулю элемента.'''
import random   # импортирую модуль для генерации случайного числа

end = True  # флаг-переключатель
nums = []   # массив для начальных даннх
i = 0
while i <= 14:
    rnd = random.randint(1, 100)
    nums.append(rnd)
    i += 1

max_module = max(nums)  # максимальное число по модулю
last_object = nums[-1]  # Последний элемент в массиве
ind = nums.index(max_module)    # Индекс последнего элемента в массиве

for j in nums:  # проверяю на последний элемент
    if max_module == last_object:
        end = False
        print(f"Исходный массив: {nums}.")
        print("Максимальное по модулю число, стоит последним в списке.")
        break

if end != False:
    new_nums = nums[ind + 1::]  # копирую срез из начального массива
    proizvedenie = 1    # Перемиенная для подсчета произведения элементов
    for k in new_nums:
        proizvedenie *= k
    print(f"Исходный массив: {nums}.")
    print(f"Максимальное по модулю число: {max_module}")
    print(f"Произведение элементов: {proizvedenie}.")
print("Программа завершила работу...")

'''
В данном упражнении вы должны написать программу для подсчета
среднего значения всех введенных пользователем чисел. Индикатором
окончания ввода будет служить ноль. При этом программа должна выдавать соответствующее сообщение об ошибке, если первым же введенным
пользователем значением будет ноль.
'''
result = 0
counter = 0
userInput = ''
while userInput != 0:
    userInput = int(input("Enter s number... "))
    if result == 0 and userInput == 0:
        print("Error!")
        break
    elif result != 0 and userInput == 0:
        result = result / counter
        print(f"Result: {round(result, 0)}")
        print("Ending programm")
        break
    else:
        result += userInput
        counter += 1
print("End.")

# Task 1
day = input("Enter a day... ")
month = input("Enter a month... ")
print(f"Today {day}, month {month}.")

# Task 2
currentYear = 2024
yearOfBurthday = int(input("Enter year... ")) # привожу строковое значение к числовому
print(f"Your {currentYear - yearOfBurthday} years old.")

# Task 3
kilometersInMile = 1.6
mile = float(input("Enter a mile... "))
result = mile * kilometersInMile
print(f"{mile} miles is {result} kilometers.")

# Task 4
maxPow = int(input("Enter max power"))
power = [2 ** i for i in range(0, maxPow + 1)]
print(power)

# Task 5
maxLenght = int(input("Enter a lenght list... ")) # maximum list length
numsList = [i for i in range(0, maxLenght + 1) if i % 5 == 3]
print(numsList)
print(list(reversed(numsList))) # the inverted list

# Task 6
number = int(input("Enter a number... "))
if number % 3 == 0:
    print("Yes!")
else:
    print("Nope")

# Переводит градусы цельсия в фаренгейты до 100
degrees = int(input("Enter number of degrees... "))

for i in range(0, degrees + 1):
    tempFarengeit = int(((1.8) * (i)) + 32)
    if i % 10 == 0:
        print(f"Celsium: {i} degrees - Farengeith: {tempFarengeit} degrees.")

# Задача 67
while True:
    userInput = input("Enter a yeras old... ")
    if userInput == '':
        print("Exit.")
        break
    userInput = int(userInput)
    if userInput <= 2:
        print("No money")
    elif 3 <= userInput <= 12:
        print("Price: 14.00$")
    elif 18 <= userInput < 65:
        print("Price: 23.00$")
    else:
        print("Price: 18.00$")

# Задача 72
print("Let's start the game!")
print("One!")
for i in range(2, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz - Buzz!...")
    elif i % 3 == 0:
        print("Fizz...")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(str(i))

# Задача 74 таблица умножения
# (напечатать цифры сверху и сбоку не решил)
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=' ')
        if j == 10:
            print()


#  количество цифр в числе
#
num = input("Enter a number... ")
z = one = two = three = four = five = six = seven = eigth = nine = 0
for c in num:
    if c == '0':
        z += 1
    elif c == '1':
        one += 1;
    elif c == '2':
        two += 1
    elif c == '3':
        three += 1
    elif c == '4':
        four += 1
    elif c == '5':
        five += 1
    elif c == '6':
        six += 1
    elif c == '7':
        seven += 1
    elif c == '8':
        eigth += 1
    elif c == '9':
        nine += 1
print(f"Zero: {z}\nOne: {one}\nTwo: {two}\nThree: {three}\nFour: {four}\nFive: {five}\nSix: {six}\nSeven: {seven}\n"
      f"Eigth: {eigth}\nNine: {nine}")


# Задача 2. Книга Васильева
# пользователь вводит целое число,
# а программа каждую цифру в этом числе меняет на «дополнение до 9»
#
nums = input("Enter a number... ")
for num in nums:
    print(num, end=" ")

dop = ''
for num in nums:
    num = int(num)
    res = 9 - num
    dop += str(res) + " "
print(f'\n{dop}')


# Задача 3. Книга Васильева
# на основе списка из натуральных чисел
# формирует целое число. Число формируется «объединением» элементов списка
#
nums = [3, 56, 367, 24, 6]
numsString = ''
for num in nums:
    n = str(num)
    numsString += ''.join(n)
print(numsString)


# Задача 4. Книга Васильева
# Напишите программу, в которой сравниваются (на предмет равенства) два числовых списка.
# Два списка равны, если они одинакового размера и у них совпадают соответствующие элементы.
#
nums = eval(input("Enter a nums list... "))
numsTwo = eval(input("Enter a nums list two... "))
length = False
objects = False
if len(nums) == len(numsTwo):
    length = True
    for i in range(0, len(nums)):
        if nums[i] == numsTwo[i]:
            continue
            objects = True
        else:
            objects = False
            break
else:
    length = False
if length and objects:
    print("Yes")
else:
    print("No")

# Задача 5. Книга Васильева
# Пользователь вводит список целочисленных значений, а также верхнюю границу для вычисления суммы.
# Программа вычисляет сумму натуральных чисел, но за исключением
# тех, которые входят в список. Например, если пользователь ввел список
# [2,5,6] и 10 в качестве верхней границы суммы, то программа должна
# вычислить сумму чисел от 1 до 10, но без учета чисел 2, 5 и 6.
#
numsList = eval(input("Enter a nums list... "))
num = eval(input("Enter a number... "))
summ = 0
equalize = False  # равны ли значения
for i in range(1, num + 1):
    for j in numsList:
        if j == i:
            equalize = False
            break
        else:
            equalize = True
            continue
    if not equalize:
        continue
    else:
        summ += i

print("Summ of numbers: " + str(summ))

# Задача 6. Книга Васильева
# Напишите программу, в которой пользователь вводит три числа,
# а программа определяет, может ли существовать треугольник со сторонами, длина которых равняется введенным значениям.
# Условие существования треугольника такое: сумма двух любых (из трех введенных) чисел должна быть больше третьего числа.
#
AB = int(input("Enter a first number... "))
AC = int(input("Enter a second number... "))
BC = int(input("Enter a threed number... "))
textYes = 'Yes'
textNo = 'No'

if AB + BC > AC and AC + BC > AB and AB + AC > BC:
    print(textYes)
else:
    print(textNo)

# Задача 7. Книга Васильева
# пользователь вводит три целых числа, а программа проверяет,
# являются ли эти числа тремя последовательными элементами арифметической последовательности.
# В арифметической последовательности каждый новый член получается прибавлением
# к предыдущему определенного фиксированного числа.
#
fixNum = 1
a = int(input("Enter a num... "))
b = int(input("Enter a num... "))
c = int(input("Enter a num... "))

if a + fixNum == b and b + fixNum == c:
    print("yes")
else:
    print("no")

# Задача 8. Книга Васильева
# пользователь вводит целое число
# от 1 до 7 включительно, а программа выводит название дня недели, соответствующее этому числу ('Понедельник' для 1,
# "Вторник" для 2, и так далее).
#
numberOfDay = int(input("Enter a number... "))
if numberOfDay == 1:
    print("Понедельник")
elif numberOfDay == 2:
    print("Вторник")
elif numberOfDay == 3:
    print("Среда")
elif numberOfDay == 4:
    print("Четверг")
elif numberOfDay == 5:
    print("Пятница")
elif numberOfDay == 6:
    print("Суббота")
elif numberOfDay == 7:
    print("Воскресенье")

# Задача 9. Книга Васильева
# пользователь вводит два действительных числа, а программа проверяет, какие из чисел больше.
# Используйте тернарный оператор и обработку исключительных ситуаций.
#
inputUser = False
number = ''
numberTwo = ''
while not inputUser:
    try:
        number = float(input("Enter a number... "))
    except:
        print("Type Error")
        inputUser = False
    try:
        numberTwo = float(input("Enter a number... "))
    except:
        print("Type Error")
        inputUser = False

    inputUser = True if type(number) == float and type(numberTwo) == float else False

result = "Число A больше числа B" if number > numberTwo else 'Число B больше числа А'
print(f"{result}\nNumber A: {number}\nNumber B: {numberTwo}")

# Задача 10. Книга Васильева
# Напишите программу для решения уравнения Ax = B – A – 1. Параметры A и B вводятся пользователем.
# Уравнение имеет решение x = (B – 1) / A – 1 если A ≠ 0.
# При A = 0 и B = 1 решением является любое число, а при A = 0 и B ≠ 1 решений у уравнения нет.
# Предложите разные варианты программы, в том числе и с использованием обработки исключительных ситуаций.
#
inputU = False
a = ''
b = ''
x = 0
while not inputU:
    try:
        a = int(input("Enter a number... "))
    except:
        print("Type Error")
        inputU = False
    try:
        b = int(input("Enter a number... "))
    except:
        print("Type Error")
        inputU = False

    inputU = True if type(a) == int and type(b) == int else False

if a != 0:
    x = (b - 1) / (a - 1)
    print(f'X = {x}')
elif a == 0 and b == 1:
    print(f"При А = {a} и B = {b}, решением является любое число.")
elif a == 0 and b != 1:
    print("Решений нет")
