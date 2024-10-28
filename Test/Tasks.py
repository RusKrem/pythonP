# Напишите программу, которая будет запрашивать у пользователя целочисленные значения и сохранять их в виде списка.
# Индикатором окончания ввода значений должен служить ноль.
# Затем программа должна вывести на экран все введенные пользователем числа (кроме нуля) в порядке возрастания –
# - по одному значению в строке. Используйте для сортировки либо метод sort, либо функцию sorted.
#
nums = [] # List for nums
while True:
    try:
        userInput = int(input('Enter a number... '))
        if userInput == 0:
            break
        else:
            nums.append(userInput)
            print(f'Number {userInput} added in list.')
    except:
        print('Error data type!')

print("\nThe data has been added. I'm sorting the list...")
nums = sorted(nums) # Sort list

# I will display the list items one at a time
for i in nums:
    print(i)

print('\nThe list items are in descending order...')
nums = reversed(nums)
for i in nums:
    print(i)
