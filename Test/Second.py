# Напишите функцию,
# создающую копию списка с исключенными из него n наибольшими и наименьшими значениями и возвращающую ее в качестве результата.
# Порядок следования элементов в измененном списке не обязательно должен в точности совпадать с источником.
# В основной программе должна быть продемонстрирована работа вашей функции.
# Для начала попросите пользователя ввести целые числа,
# затем соберите их в список и вызовите написанную вами ранее функцию.
# Выведите на экран измененную версию списка вместе с оригинальной.
# Если пользователь введет менее четырех чисел, должно быть отображено соответствующее сообщение об ошибке.
#
def delete_min_max_elements(numsList):
    new_set = set(numsList) # I will filter out the same values
    new_List = list(new_set) # Creating a new list
    min_el = min(numsList) # I get the minimum element
    max_el = max(numsList) # I get the maximum element

    # I'm deleting the min and max values
    for i in new_List:
        if i == min_el:
            new_List.remove(i)
        elif i == max_el:
            new_List.remove(i)


    return sorted(new_List)

nums = []  # List for nums
while True:
    try:
        userInput = int(input('Enter a number.(Enter zero to stop)... '))
        if userInput == 0:
            if len(nums) < 4:
                print('The length of the list is less than four!')
                continue
            break
        else:
            nums.append(userInput)
            print(f'Number {userInput} added in list.')
    except:
        print('Error data type!')

print(delete_min_max_elements(nums))

nums_L = [1, 2, 1, 4, 5, 5, 6, 1, 16, 24, 24, 5, 13, 31, 1, 2, 3]

print('\nA list without a minimum and maximum value:')
print(delete_min_max_elements(nums_L))