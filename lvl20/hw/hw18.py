#18)შეიყვანეთ რიცხვი და გამოიყენეთ while ციკლი, რომ შეამოწმოთ, არის თუ არა რიცხვი დადებითი.

a = int(input("num"))

while a>0:
    print("positive")
    break
while a<0:
    print("negative")
    break

while a==0:
    print("0")
    break