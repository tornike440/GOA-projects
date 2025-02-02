import random

list=[]

for i in range (0,10):
    list.append(random.randint(0,100))

sum=0

for i in range (0,len(list)):
    sum=sum+list[i]
print(sum)