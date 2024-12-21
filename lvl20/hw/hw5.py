#6)დაბეჭდე რიცხვები 1-დან 30-მდე, და გვერდით მიუწერე "ლუწია" თუ "კენტია".
for i in range(0,30):
    if i %2==0:
        print(str(i)+"even")
    else:
        print(str(i)+"odd")