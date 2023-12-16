#Random Password Generator App

import random

#Create lists of letters, numbers, and characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Intro
print('Welcome to the PyPassword Generator!')
#Inputs
numLetters = input('How many letters would you like in your password? \n')
numSymbols = input('How many symbols would you like? \n')
numNumbers = input('How many numbers would you like? \n')

passwordList = []
#Generate letters
for n in range(0, int(numLetters)):
    j = random.randint(0, len(letters) - 1)
    char = letters[j]
    passwordList.append(char)
#Generate symbols
for n in range(0, int(numSymbols)):
    j = random.randint(0, len(symbols) - 1)
    char = symbols[j]
    passwordList.append(char)
#Generate numbers
for n in range(0, int(numNumbers)):
    j = random.randint(0, len(numbers) - 1)
    char = numbers[j]
    passwordList.append(char)

#Shuffle characters
random.shuffle(passwordList)
password = ""
#Create password from chosen characters
for char in passwordList:
    password += char
print(f'Your password is: {password}')
