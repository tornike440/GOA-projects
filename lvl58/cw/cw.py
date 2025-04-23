def minus(a, b):
    if a%2==0:
        a=a//2
    else:
        a=a+1
    
    return a-b
#returnis magivrad rom damewera print mashin 
# shedegze shemdgom operaciebis shesruleba sheuzlebeli iqneboda
print(minus(5, 3)) # 2
print(minus(4, 2)) # 0



#lower() funqcia daaapataravebs yvela simbolos nebismier shemtxvevashi
print("HELLO".lower()) #
print("hello".lower()) # hello
print("Hello".lower()) # hello

#upper() funqcia gaadidebsa yvela simbolos nebismier shemtxvevashi
print("hello".upper()) # HELLO
print("HELLO".upper()) # HELLO
print("Hello".upper()) # HELLO

#capitalize() funqcia gaadidebs pirvel elements da daapataravebs danarchenebs
print("hello".capitalize()) # Hello
print("HELLO".capitalize()) # Hello
print("Hello".capitalize()) # Hello


def findcapitals(word):
    capitals = []
    for i in range(len(word)):
        if word[i].upper() == word[i]:
            capitals.append(word[i])
    return capitals





#(capitalize("abcdef"),['AbCdEf', 'aBcDeF'])


def capitalize(s):
    word1 = ""
    word2 = ""
    list1 = []
    for i in range(len(s)):
        if i % 2 == 1:
            word1 += s[i].upper()
        else:
            word1 += s[i].lower()

    for i in range(len(s)):
        if i % 2 == 0:
            word2 += s[i].upper()
        else:
            word2 += s[i].lower()

    list1.append(word1)
    list1.append(word2)
    return list1
            

