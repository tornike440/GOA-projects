
def upperit(a):
    flag=1
    answer=[]
    for i in range (0,len(a)):
        if flag == 1:
            answer.append(a[i].upper())
            flag=0
        elif flag == 0:
            answer.append(a[i].lower())
            flag=1
        #If the character is not an alphabet letter, leave it unchanged and reset the flag to 1.
        if a[i].isalpha() == False:
            flag=1

    return "".join(answer)
        
