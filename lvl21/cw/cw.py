# a= int(input("num:"))

# ans=input("dabbewdo luwi tu kenti")

# b=0
# c=0

# for i in range(0,a+1):
#     if i%2==0:
#         b +=i
#     else:
#         c+=i

    
# if ans=="luwi":
#     print(b)
# elif ans=="kenti":
#     print(c)
# else:
#     print("dabewdo")

a=int(input("num:"))

i=0
su3m=0
su5m=0

while i<a:
    if i%3==0:
        su3m += i
    elif i%5==0:
        su5m += i

    i +=1

print(su3m)
print(su5m)






