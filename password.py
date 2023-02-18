def passwordGenerator(choice: str='strong') -> str:
    """
    Returns generated password.
    """

    import random

    passlist = []

    if choice == 'weak':
        wordlist = ['password', 'drowssap', '123', 'strong', 'weak',
                    '45301', 'text', 'some', 'word', 'random', 'idea']

        c = random.randint(1, 3)

        for i in range(c):
            passlist.append(random.choice(wordlist))

        password = ''.join(passlist)
                       
    elif choice == 'strong':
        length = random.randint(1, 7) + 7

        symbol = False
        number = False
        bletter = False
        sletter = False

        for i in range(length):

            c = random.randint(1, 6)

            if c == 1:
                l = chr(random.choice([33, 35, 36, 37, 38, 63, 64]))
                symbol = True
            elif c == 2:
                l = chr(random.randint(48, 57))
                number = True
            elif c in [3, 4]:
                l = chr(random.randint(65, 90))
                bletter = True
            else:
                l = chr(random.randint(97, 122))
                sletter = True

            passlist.append(l)

        if not (symbol and number and bletter and sletter):
            password = passwordGenerator()

        password = ''.join(passlist)

    else:
        print('Wrong argument, write "strong" or "weak".')
        return

    return password


if __name__=="__main__":

    s = input('Would you like a strong or a weak password? ')
    password = passwordGenerator(s)
    print('Password generated for you: ', password)
