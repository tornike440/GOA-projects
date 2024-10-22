a = input("enter your birth year ")

b= int(a)

if (2024 -b ) >= 18:
    print("you are full grown adult, born in " + a)
else:
    print("you are still teenage, born in " + a)

month = input("your birth month ")

ex_age = ((2025*12-2)-(int(b)*12+int(month)))

ex_agem = ex_age / 12

print("you should be "+ str(ex_agem)+" years old")
