
def character():
    user_input = input('Type a word? ')
    user_input = user_input.lower()
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for letter in user_input:
        if letter in alphabet:
            print(letter, end=' ')
            print(alphabet.index(letter))
        else:
            print('TRY AGAIN FOOL!')
character()