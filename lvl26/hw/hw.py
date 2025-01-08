import random

attempts=[]

ran_num= random.randint(0,200000)

a= int(input("guess number"))
while a!= ran_num:
    attempts.append(a)
    if a>ran_num:
        print("guess lower")
    else:
        print("guess higher")
    a= int(input("guess number"))
print("you guessed correctly")
print(f"you guessed {len(attempts)} attempts")
print("here are all your guesses")
print(attempts[:])
