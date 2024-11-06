# Дан список чисел.
# Используя функцию enumerate() в заголовке цикла for,
# создайте второй список, в котором каждый элемент должен быть строкой,
# включающей через пробел индекс и значение соответствующего элемента первого списка.

no_empty_list = [2, 3, 3, 5, 12, 124, 45, 75, 63]
string_list = []
for num, value in enumerate(no_empty_list):
    my_string = "Index: " + str(num) + " | " + "Value: " + str(value)
    string_list.append(my_string)

print(string_list)