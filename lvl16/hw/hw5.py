#5) დედამ გაგიშვათ აფთიაქში თავის ტკივილის წამლის საყიდლათ, 
# ეს წამალი დღეში უნდა დალიო შენი წონის მიხედვით. თუ 10 დან
#  20 კილომდე ხარ ნახევარი ტაბლეტი უნდა დალიო დღეში, თუ 
# 20-44 კილომდე ხარ 1 ტაბლეთი ორჯერ დღეში და თუ 45 კილოზე
#  მეტი ხარ სამი ტაბლეტი უნდა დალიო ორჯერ დღეში
# . თქვენი მისიაა ამ ინფორმაციით გაარკვიოთ მომხარებელს რამდენი წამალი
#  აქვს დასალევი და დღეში რამდენჯერ უნდა დალიოს.

a=int(input("weight"))

if 10<=a<=20:
    print("half a tablet once a day")
elif 20<a<=45:
    print("2 tablets twice a day")
elif a>45:
    print("3 tablets twice a day")