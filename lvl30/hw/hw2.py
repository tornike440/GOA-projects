#3) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, დაპრინტეთ ყველა რიცხვი მაგრამ მიუწერეთ რომელია კენტი და რომელია ლუწი
list=[1,2,3,4,5,6,7,8,9,10]
#print(f"{list[0::2]} kenti,{list[1::2]} luwi")
for i in range(0,10,2):
    print(str(list[i])+"kenti, "+str(list[i+1])+"luwi,")