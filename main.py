import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
numLetters = input('How many letters would you like in your password? \n')
numSymbols = input('How many symbols would you like? \n')
numNumbers = input('How many numbers would you like? \n')
totalNum = int(numLetters) + int(numSymbols) + int(numNumbers)

passwordList = []
letterCount, symbolCount, numberCount = 0, 0, 0
for n in range(0, int(totalNum)):
    choice = random.randint(0, 2)
    if choice == 0 and letterCount < int(numLetters):
        j = random.randint(0, len(letters) - 1)
        char = letters[j]
        letterCount += 1
    elif choice == 1 and symbolCount < int(numSymbols):
        j = random.randint(0, len(numbers) - 1)
        char = numbers[j]
    else:
        j = random.randint(0, len(symbols) - 1)
        char = symbols[j]
    passwordList.append(char)

password = ""
for char in passwordList:
    password += char
print(f'Your password is: {password}')