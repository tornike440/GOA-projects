#6) მომხმარებელს შემოატანინეთ 5 რიცხვი და დაამატეთ ეს რიცხვები სიაში, ბოლოს გამოიტანეთ ტერმინალში ეს სია 
list=[]

for i in range (0,5):
    num=input("num: ")
    try:
        num/6
    except:
        print("please enter integer")
    list.append(num)