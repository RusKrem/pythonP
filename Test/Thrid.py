# В данном упражнении вам предстоит разработать программу, в которой
# у пользователя будет запрошен список слов, пока он не оставит строку
# ввода пустой.
# После этого на экране должны быть показаны слова, введенные пользователем, но без повторов, – каждое по одному разу.
# При этом слова должны быть отображены в том же порядке, в каком их вводили с клавиатуры.
# Например, если пользователь на запрос программы введет следующий список слов:

# first
# second
# first
# third
# second

# программа должна вывести:
# first
# second
# third
#

words = []
new_words = []
while True:
    try:
        userInput = str(input('Enter a word.(Press enter to stop)... '))
        if userInput == '':
            break
        else:
            words.append(userInput)
            print(f'Word {userInput} added in list.')
    except:
        print('Error data type!')

for i in range(0, len(words)):
    if words[i] in new_words:
        continue
    else:
        new_words.append(words[i])

print(new_words)