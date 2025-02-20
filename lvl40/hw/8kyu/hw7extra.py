#Given an array of numbers (in string format), you must return a string. 
# The numbers correspond to the letters of the alphabet in reverse order:
#  a=26, z=1 etc. You should also account for '!', '?' and ' ' 
# that are represented by '27', '28' and '29' respectively.


#All inputs will be valid.


def switcher(arr):
    answer=[]
    for i in range(0,len(arr)):
        if int(arr[i]) == 29:
            answer.append(" ")
        elif int(arr[i]) == 28:
            answer.append("?")
        elif int(arr[i]) == 27:
            answer.append("!")
        elif int(arr[i]) == 26:
            answer.append("a")
        elif int(arr[i]) == 25:
            answer.append("b")
        elif int(arr[i]) == 24:
            answer.append("c")
        elif int(arr[i]) == 23:
            answer.append("d")
        elif int(arr[i]) == 22:
            answer.append("e")
        elif int(arr[i]) == 21:
            answer.append("f")
        elif int(arr[i]) == 20:
            answer.append("g")
        elif int(arr[i]) == 19:
            answer.append("h")
        elif int(arr[i]) == 18:
            answer.append("i")
        elif int(arr[i]) == 17:
            answer.append("j")
        elif int(arr[i]) == 16:
            answer.append("k")
        elif int(arr[i]) == 15:
            answer.append("l")
        elif int(arr[i]) == 14:
            answer.append("m")
        elif int(arr[i]) == 13:
            answer.append("n")
        elif int(arr[i]) == 12:
            answer.append("o")
        elif int(arr[i]) == 11:
            answer.append("p")
        elif int(arr[i]) == 10:
            answer.append("q")
        elif int(arr[i]) == 9:
            answer.append("r")
        elif int(arr[i]) == 8:
            answer.append("s")
        elif int(arr[i]) == 7:
            answer.append("t")
        elif int(arr[i]) == 6:
            answer.append("u")
        elif int(arr[i]) == 5:
            answer.append("v")
        elif int(arr[i]) == 4:
            answer.append("w")
        elif int(arr[i]) == 3:
            answer.append("x")
        elif int(arr[i]) == 2:
            answer.append("y")
        elif int(arr[i]) == 1:
            answer.append("z")
    return "".join(answer)



