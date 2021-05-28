import random
x = random.randint(1,20)
y = int(input('Guess your lucky number:'))
while True:
    if x == y:
      print('you win')
      break
    else: 
        print('winning number',x)
        x = random.randint(1,20)
        y = int(input('Guess your lucky number:'))
          y = input('want to guess another number?')
          while True:
                if x == y:
                  print('you win')
                  break
                else: 
                print('winning number',x)
          x = random.randint(1,20)
          y = int(input('Guess your lucky number:'))
      else:
      break
