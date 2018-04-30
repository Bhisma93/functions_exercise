user_input = input('Type a word: ')
user_input = user_input.title()
vowels = ['a','e','i','o','u']

def long_vowels():
    for letter in user_input:
        if letter in vowels:
            print(letter * 5, end='')
        else:
            print(letter, end='')
long_vowels()