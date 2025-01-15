#7) დაიწყეთ რიცხვების სიით, გამოიყენეთ while loop რომ წაშალოთ ყველა რიცხვი ამ სიიდან და გამოიყენეთ pop რო დაპრინტოთ ეს ყველა ელემენტი სანამ ლისტი არ დაცარიელდება 
import random
list=[]
for i in range(0,10):
    a=random.randint(0,100)
    list.append(a)
b=len(list)
print(list)
trys=[]
while b!=0:
    pop=int(input("num:"))
    try:
        list.remove(pop)
    except ValueError:
        print("this number is not on the list. try again")
    trys.append(pop)
    b=len(list)
    print(b)

print("CONGRATS!!")
print(f"you needed {len(trys)} numbers of tries to get all the 10 hidden numbers")

