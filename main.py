import random

print('Welcom To Your Password Generator')

chars = ''

number = input('Amount of passwords to generate: ')
numer = int(number)

length = input('Input your password length: ')
length = int(length)

print('\nhere are your paswords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
