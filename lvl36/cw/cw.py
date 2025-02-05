def multiply(a,b):
    result=a*b
    if result&2==0:
        print(f"result is {result} and it is even")
    else:
        print(f"result is {result} and it is odd")

num1=int(input("num:"))

num2=int(input("num:"))

multiply(num1,num2)

