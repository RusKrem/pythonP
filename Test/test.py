import random

# 1. Дан массив A целых чисел, содержащий 30 элементов.
# Вычислить и вывести количество и сумму тех элементов, которые делятся на 5 и не делятся на 7.
number_l = [1, 25, 778, 325, 4, 6654, 12, 33, 74, 14, 65, 56, 17, 34, 697, 0, 317, 79, 3177, 2, 9, 36, 35]

def summ_elements(number_list):
    """Returns the number and sum of those elements
    that are divisible by 5 and not divisible by 7."""

    summ = 0
    count_elements = 0
    for num in number_list:
        if num % 5 == 0 and num % 7 != 0:
            summ += num
            count_elements += 1
    return f"Элементов в массиве: {count_elements} | сумма элементов: {summ}."

print('Задача 1:')
func_one = summ_elements(number_l)
print(func_one)

# 2. Дан массив A вещественных чисел, содержащий 25 элементов.
# Вычислить и вывести число отрицательных элементов и число членов, принадлежащих отрезку [1,2]
def number_of_negative_elements(list_length):
    """outputs the number of negative elements
    and the number of terms belonging to the segment [1,2]"""

    count = 0
    odd_numbers = 0
    on_the_one_two_segment = 0
    real_numbers = []
    while count < list_length:
        number = random.uniform(-2, 2)
        if number < 0:
            odd_numbers += 1
        elif 1 < number < 2:
            on_the_one_two_segment += 1
        real_numbers.append(number)
        count += 1
    return f"Length array: {list_length} | odd elements: {odd_numbers} | on the 1-2 segment: {on_the_one_two_segment}."

print("\nЗадача 2.")
print(number_of_negative_elements(25))

# 3. Дан массив K целых чисел, содержащий 35 элементов.
# Вычислить и вывести R=S+P,
# где S – сумма четных элементов, меньших 3, P – произведение нечетных элементов, больших 1.
def calculate_summ():
    """Calculates and outputs R=S+P,
    where S is the sum of even elements less than 3,
    P is the product of odd elements greater than 1."""

    sum_of_even_elements = 0
    product_of_odd_elements = 1
    for i in range(0, 36):
        number = random.randint(-10, 10)
        if number % 2 == 0 and number < 3:
            sum_of_even_elements += number
        elif number % 2 != 0 and number > 1:
            product_of_odd_elements *= number
    summ_ele = sum_of_even_elements + product_of_odd_elements
    return f"R = {sum_of_even_elements} + {product_of_odd_elements} = {summ_ele}"

print("\nЗадача 3.")
print(calculate_summ())