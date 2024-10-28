# Напишите программу, запрашивающую у пользователя целые числа, пока он не оставит строку ввода пустой.
# После окончания ввода на экран должны быть выведены сначала все отрицательные числа, которые были введены,
# затем нулевые и только после этого положительные.
# Внутри каждой группы числа должны отображаться в той последовательности, в которой были введены пользователем.
# Например, если он ввел следующие числа:
# 3, -4, 1, 0, -1, 0 и -2, вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1.
# Каждое значение должно отображаться на новой строке.
#
nums = []
sort_num_list = []
while True:
    try:
        userInput = input("Enter a number... ")
        if userInput == '':
            break
        else:
            nums.append(int(userInput))
    except:
        print("Error data type.")

for i in range(0, len(nums)):
    if nums[i] < 0:
        sort_num_list.append(nums[i])
for j in nums:
    if j == 0:
        sort_num_list.append(j)
for k in nums:
    if k > 0:
        sort_num_list.append(k)
print('Original array:')
print(nums, "\n")
print('Sorted array:')
print(sort_num_list)