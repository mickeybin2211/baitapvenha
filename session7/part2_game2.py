from random import *
a = randint(0,100)
b = randint(0,100)
c = randint(-2,2)

result_true = a + b
result_display = result_true + c
print(a, " + ", b, " = ", result_display)

answer = input("Yes / No: ").lower()
if c == 0:
    if (answer == 'yes'):
        print("You Right!")
    elif (answer == 'no'):
        print("You Wrong!")
    else:
        print("Nhap Yes Hoac No")
else:
    if (answer == 'yes'):
        print("You Wrong!")
    elif (answer == 'no'):
        print("You Right!")
    else: 
        print("Yes or No")
