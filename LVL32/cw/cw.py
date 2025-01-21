import random
list=[]
for i in range(0,10):
    a=random.randint(0,100)
    list.append(a)
#print("list")

for i in range(0,10):
    if list[i]%3==0:
        print(f"{list[i]} can be devided by 3")
    elif list[i]%5==0:
        print(f"{list[i]} can be devided by 5")
    else:
        print(list[i])