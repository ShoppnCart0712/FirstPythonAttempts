#just messin around
greeting = "Hey there you."
print (greeting)
name = input ("Give me your name. ")
print(greeting.replace("you" ,name))
birth_year = input("When were you created? ")
age = 2024 - int(birth_year)
print(f"You're {age}, you old fart.")

import random

x= 3
x *= 3
print(x)
print(x==9)
x = 5
while x > 0:
    temp = random.randint(0,120)
    print("Tempurature is "+ str(temp) + ".")
    if temp > 100 :
        print("may god have mercy on your soul")
    elif temp > 60:
        print ("hot hot hot")
    elif temp > 30:
        print ("perfect")
    else:
        print ("freeze")
    x -= 1