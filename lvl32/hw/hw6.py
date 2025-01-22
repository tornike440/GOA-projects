import random
list=[]
for i in range(0,10):
    a=random.randint(0,100)
    list.append(a)

print(list)

for i in range(0,len(list)):
    if list[i]%2==1:
        list.remove(list[i])