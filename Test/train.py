import math
import random

def array_generate(array_length):
    """
    This function returns an array of positive and negative numbers
    with a long array_length.
    And returns an empty array if array_length = 0
    :param array_length:
    :return: new list -100 : 100
    """

    new_array = []
    counter = 0
    if array_length == 0:
        return new_array
    else:
        while counter < array_length:
            number = random.randint(-100, 100)
            new_array.append(number)
            counter += 1

    return new_array

def array_generate_positive_numbers(array_length):
    """
    This function returns an array of positive and negative numbers
    with a long array_length.
    And returns an empty array if array_length = 0
    :param array_length:
    :return: new list 0 : 100
    """

    new_array = []
    counter = 0
    if array_length == 0:
        return new_array
    else:
        while counter < array_length:
            number = random.randint(0, 100)
            new_array.append(number)
            counter += 1

    return new_array

# Дан массив, содержащий 10 элементов. Вычислить произведение
# элементов, стоящих после первого отрицательного элемента. Вывести
# исходный массив и результат вычислений.
my_arr = array_generate(10)
def calculate_the_product(new_list):
    """
    Calculates the product of the elements after the first negative element.
    Outputs the source array and the result of calculations.
    :param new_list: list
    :return: int summ elements
    """

    list_slice = []
    list_slice_summ = 0
    for num in range(0, len(new_list)):
        if new_list[num] < 0:
            list_slice = new_list[num + 1 : ]
            list_slice_summ = sum(new_list[num + 1 : ])
            break

    return f"List: {new_list}\nslice list: {list_slice}\nsumm elements: {list_slice_summ}."

print("Test function:")
array_info = calculate_the_product(my_arr)
print(array_info)

# 1. Составить программу для вычисления площади разных геометрических фигур.
def area_geometric_shapes_calculate(shape, **kwargs):
    """
    This function calculates the area of different geometric shapes
    :param shape: name of geometric shape
    :param kwargs: keys: a - side_1, b - side_2, h - height, r - radius
    :return: string - area shapes
    """

    area = None
    try:
        if shape == 'triangle':
            area = 0.5 * (kwargs['a'] * kwargs['h'])
            return round(area, 2)
        elif shape == 'square':
            area = kwargs['a'] * kwargs['a']
            return round(area, 2)
        elif shape == 'rectangle':
            area = kwargs['a'] * kwargs['b']
            return round(area, 2)
        elif shape == 'circle':
            area = math.pow(kwargs['r'], 2) * math.pi
            return round(area, 2)
    except KeyError:
        return area

triangle = area_geometric_shapes_calculate('triangle', a = 5, h = 3)
square = area_geometric_shapes_calculate('square', a = 5)
rectangle = area_geometric_shapes_calculate('rectangle', a = 4, b = 3)
circle = area_geometric_shapes_calculate('circle', r = 3.8)
err = area_geometric_shapes_calculate('d')
print("\nTest function 1:")
print(f"Triangle area: {triangle}\nSquare area: {square}\nRectangle area: {rectangle}\nCircle area: {circle}\n"
      f"Erroneous input: {err}")


# 2. Даны 3 различных массива целых чисел (размер каждого не превышает 15).
# В каждом массиве найти сумму элементов и средне арифметическое значение.

array_one = array_generate_positive_numbers(15)
array_two = array_generate_positive_numbers(15)
array_three = array_generate_positive_numbers(15)

def calculate_summ_elements_in_list(*args):
    """
    Returns the sum of the elements and the arithmetic mean.
    :param args: 3 lists
    :return: summ elements
    """
    
    summ_one = sum(args[0])
    summ_two = sum(args[1])
    summ_three = sum(args[2])
    ar_one = round((summ_one / len(args[0])), 2)
    ar_two = round((summ_two / len(args[1])), 2)
    ar_three = round((summ_three / len(args[2])), 2)

    return (f"Summ one {summ_one}, Summ two: {summ_two}, Summ three: {summ_three}\n"
            f"Ar one: {ar_one}, Ar two: {ar_two}, Ar three: {ar_three}")

print("\nTest function 2:")
arrays_summ = calculate_summ_elements_in_list(array_two, array_two, array_three)
print(arrays_summ)

# 3. Вычислить площадь правильного шестиугольника со стороной, а,
# используя подпрограмму вычисления площади треугольника.

def calculating_area_regular_hexagon(side):
    """
    Calculate the area of a regular hexagon with a side, a,
    through the triangle area calculation function.
    :param side: the side of an equilateral triangle
    :return: the area of a regular hexagon
    """

    hexagon_area = 6 * (calculation_area_equilateral_triangle(side))

    return f"The area of a regular hexagon is: {round(hexagon_area, 2)}"

def calculation_area_equilateral_triangle(triangle_side):
    """
    Calculates the area of an equilateral triangle
    :param triangle_side: the side of an equilateral triangle
    :return: the area of an equilateral triangle
    """

    area = (math.pow(triangle_side, 2) * math.sqrt(3)) / 4

    return area

print("\nTest function 3:")
my_area = calculating_area_regular_hexagon(6)
print(my_area)