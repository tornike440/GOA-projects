car_List= ["nissan gt-rs","porche gt-3rs", "cls63", "cls53", "m35", "x6","buggati veiron", "lamborgini aventador", "tesla cybertruck","tesla model 6"]

print(car_List[1])
print(car_List[4])

b=len(car_List)
if b%2==1:
    b=b-1
    c=b/2
    print(car_List[int(c)])
    print(car_List[int(c)+1])
else:
    c=b/2
    print(car_List[int(c)])

print(car_List[int(c):])

print(car_List[-3])

print(car_List[-1])

print(car_List[:])




