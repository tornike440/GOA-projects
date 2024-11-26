#6) თქვენ დაგპატიჟეს პატარა ბავშვის დაბადების დღეზე
#  გასართობ ცენტრში, თქვენთან ერთად ამ გასართობ 
# ცენტრში დაპატიჟეს 10 ადამიანი და ამ 10 ადამიანიდან ერთ 
# ერთი ნიკოლოზია. ნიკოლოზს უთხრეს რომ მას შეუძლია ბავშებთან 
# ერთად გაერთოს თუ ის ფეხსაცმელებს გაიხდის და ქურთუკს საკიდზე 
# ჩამოკიდებს (True და False-ს გამოყენება დაგჭირდებათ).
#  თქვენი მიზანია გაარკვიოთ ნიკოლოზმა შეასრულა ეს წესები თუ არა,
#  ანუ შეუძლია თუ არა მას ბავშებთან ერთად გართობა.

nika = input("chamokide qurtuki?")
while nika not in ["ki","ara"]:
    print("upasuxet ki an ara")
    nika = input("chamokide qurtuki?")

bool = nika=="ki"

nika1 = input("fexsacmeli gaixade?")
while nika1 not in ["ki","ara"]:
    print("upasuxet ki an ara")
    nika = input("fexsacmeli gaixade?")

bool1 = nika1=="ki"

if bool and bool1:
    print("shebrzandit")
elif bool and not bool1:
    print("fexsacmeli gaixade da shexvale")
elif not bool and bool1:
    print("gaixade qurtuki da shegishveb")
else:
    print("gaixade qurtuki da fexsacmeli da shegishveb")

    
