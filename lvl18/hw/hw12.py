#2)  მომხმარბელს შემოატანინეთ რიცხვი შემდეგ კი მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ რიცხვები და გვერძე მიუწერეთ ლუწია თუ კენტ
a = int(input("num:"))
for i in range (1,a):
    if i%2 == 0:
        print(f"{i}-even")
    else:
        print(f"{i}-odd")