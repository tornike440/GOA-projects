def numbers_with_digit_inside(x, d):
    numbers_list = []
    
    for i in range(1, x + 1):
        if str(d) == str(i): 
            numbers_list.append(i)
    
    return_list = []
    a = len(numbers_list)
    return_list.append(a)
    b = sum(numbers_list)
    return_list.append(b)
    
    product = 1
    if numbers_list:
        for i in range(len(numbers_list)):
            product *= numbers_list[i]
    else:
        product = 0
    
    return_list.append(product)
    
    return return_list

