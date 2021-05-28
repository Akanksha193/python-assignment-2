    import random
    x = random.randint(1,5)
    y = int(input('Guess your lucky number:'))
    while True:
        if x == y:
        print('Good Guess')
        break
        else: 
            print('winning number',x)
            x = random.randint(1,5)
            y = int(input('try again'))
        