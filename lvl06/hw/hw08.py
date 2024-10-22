



a= input("do you have wifi? ")


while a not in ["yes", "no"]:
    print("please, answer with 'yes' and 'no'")
    a= input("do you have wifi? ")
    continue


if a == "no":
    have_internet = False
else:
    have_internet = True
    


b= input("do you have board games? ")

while b not in ["yes", "no"]:
    print("please, answer with 'yes' and 'no'")
    b= input("do you have board games? ")
    continue


if a == "no":
    have_board_games = False
else:
    have_board_games = True
    



if  not have_internet and not have_board_games:
    print("well, you have a reason to be bored")

if  have_internet and  have_board_games:
    print("well you have everything to have fun with!")

if  have_internet and not  have_board_games:
    print("well you have something to have fun with!")

if  not have_internet and have_board_games:
    print("well you have something to have fun with!")