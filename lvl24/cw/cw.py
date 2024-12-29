setgmail = input("enter your gmail")

b= setgmail[::-1]

c=b[0:10]
while c not in ["moc.liamg@","ur.liam@"]:
    print("email that you entered is not real")
    setgmail = input("enter your gmail")

    b= setgmail[::-1]

    c=b[0:10]





setpassw=input("enter your password")

repassw=input("reenter it")

while setpassw!=repassw:
    print("incorect")
    c=input("reenter it")

print("succsesfully registered")

gmail= input("enter your gmail")

passw=input("enter your password")


while setgmail!=gmail or setpassw!=passw:
    print("email or password is incorrect")
    a = input("enter your gmail")

    b=input("enter your password")



