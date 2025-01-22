#4) გააკეთეთ Find Maximum და გამოიყენეთ for loop. მიზანი: სიაში უნდა იპოვოთ მაქსიმუმი ინტეჯერი მაგალითად: [1, 546, 456 ,123] => [546]

import random
list=[]
for i in range(0,10):
    a=random.randint(0,100)
    list.append(a)

print(list)

print(max(list))