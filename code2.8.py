x = str(input('enter the value:'))
u=0
v=0
for s in x:
    if s.isdigit():
        print(s)
        u+=1
    elif s.isalpha():
        print(s)
        v+=1
    else:
      pass
print('alphabets',v)
print('digit',u)