#1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი

a=int(input("num:"))

sum=0

for i in range (0, a+1):
    sum +=i

print(sum)