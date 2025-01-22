print("hi welcome to our store, GXstore")
print("here you can buy almost every part of pc")

computer_parts = [
    "Intel Core i5 Processor", "Intel Core i7 Processor", "AMD Ryzen 5 Processor", "AMD Ryzen 7 Processor",
    "Basic Motherboard", "Gaming Motherboard", "High-End Motherboard", 
    "8GB RAM Stick", "16GB RAM Kit", "32GB RAM Kit",
    "NVIDIA GTX 1650", "NVIDIA RTX 3060", "NVIDIA RTX 3080",
    "AMD RX 6500", "AMD RX 6700", "AMD RX 6800",
    "Standard CPU Cooler", "High-Performance CPU Cooler", "All-in-One Liquid Cooler",
    "500GB SSD", "1TB SSD", "2TB SSD", 
    "1TB Hard Drive", "2TB Hard Drive", "4TB Hard Drive",
    "500W Power Supply", "750W Power Supply", "850W Power Supply",
    "Basic PC Case", "Gaming PC Case", "High-End PC Case",
    "Standard Keyboard", "Gaming Keyboard", "Mechanical Keyboard",
    "Basic Mouse", "Gaming Mouse", "Wireless Mouse",
    "21-Inch Monitor", "27-Inch Monitor", "32-Inch Gaming Monitor",
    "PC Headset", "Gaming Headset", "Wireless Gaming Headset",
    "Stereo Speakers", "Gaming Speakers", "High-Quality Webcam",
    "Standard Thermal Paste", "High-Performance Thermal Paste",
    "External SSD (500GB)", "External SSD (1TB)", "External SSD (2TB)",
    "External Hard Drive (1TB)", "External Hard Drive (2TB)", "External Hard Drive (4TB)",
    "Wi-Fi Adapter", "Bluetooth Adapter", "Sound Card",
    "Case Fans (2-Pack)", "RGB Case Fans (3-Pack)", "Fan Controller",
    "Gaming Chair", "Gaming Desk", "Mouse Pad",
    "VR Headset", "Basic Surge Protector", "UPS (Uninterruptible Power Supply)",
    "Anti-Static Wrist Strap", "Cable Management Kit",
    "Memory Card Reader", "Basic Optical Drive", "External DVD Writer",
    "Portable Monitor", "Docking Station", "USB Hub (4-Port)",
    "Standard USB Flash Drive (32GB)", "High-Speed USB Flash Drive (64GB)",
    "Compact External SSD", "Gaming Console Adapter", "Streaming Capture Card",
    "Basic Webcam", "Gaming Webcam", "Ring Light",
    "RGB Light Strip", "PC Cleaning Kit", "Dust Filters for Case",
    "High-Speed Ethernet Cable", "Cable Extension Kit", "RGB Keyboard and Mouse Combo",
    "Gaming Mouse Pad", "Mechanical Keyboard Switches (Spare)", "USB-C to HDMI Adapter",
    "PC Diagnostic Tool", "Spare Screws Kit", "Portable Power Bank",
    "Basic Graphics Tablet", "Advanced Graphics Tablet", "Display Calibration Tool",
    "Extra SSD Mounting Brackets", "Basic Tool Kit", "High-End Tool Kit",
    "GPU Support Bracket", "Basic Webcam Stand", "Adjustable Monitor Arm",
    "Standard Monitor Riser", "Wireless Charger", "Smart Plug",
    "Overhead Microphone Boom Arm", "Pop Filter", "Gaming Microphone",
    "Audio Mixer", "Basic Capture Card", "4K Capture Card",
    "Basic Streaming Light", "Portable SSD (1TB)", "Portable SSD (2TB)",
    "Gaming Router", "High-Performance Router", "Basic Docking Station",
    "High-End USB-C Hub", "Portable Monitor (15-Inch)", "Compact Webcam",
    "RGB Cooling Pad", "Laptop Stand", "High-Speed NVMe SSD Adapter",
    "Portable NVMe SSD Enclosure", "PCIe Expansion Card", "VR Cable Management Kit",
    "GPU Mining Frame", "Basic PC Bench Table", "Portable Tool Case",
    "Motherboard Diagnostic Card", "Extra USB Ports Expansion", "PCIe SSD Expansion Card"
]



prices = [
    200, 300, 180, 250,
    120, 150, 200,
    40, 70, 120,
    150, 300, 700,
    130, 250, 400,
    30, 80, 150,
    50, 90, 160,
    40, 70, 130,
    50, 80, 150,
    30, 70, 120,
    20, 50, 70,
    100, 250, 400,
    40, 100, 200,
    60, 150, 250,
    15, 30,
    80, 130, 200,
    60, 100, 180,
    20, 30, 50,
    15, 50, 70,
    20, 70, 100,
    50, 90, 200,
    30, 40, 60,
    70, 150, 200,
    20, 50, 70,
    15, 25, 40,
    30, 80, 120,
    40, 50, 70,
    80, 150, 300,
    200, 300, 500,
    250, 400, 600,
    60, 120, 200,
    100, 180, 300,
    40, 50, 70,
    80, 150, 300,
    200, 300, 500,
    250, 400, 600,
    60, 120, 200,
    100, 180, 300,
    40, 50, 70,
    80, 150, 300,
    200, 300, 500,
    250, 400, 600,
    60, 120, 200,
    100, 180, 300,
    40,
]

bucket_list=[]
price=0
print("register/guest mode")
a=input("")

while a not in ["register","guest mode"]:
    print("please answer with 'register' or 'guest mode'")
    print("register/guest mode")
    a=input("")


gmail="you have not entered your mail bro"
b=gmail[::-1]
c=b[:10]


if a == "register":
    gmail= input("at this moment we only supprot gmail. please enter your gmail")
    b=gmail[::-1]
    c=b[:10]
    while c !="moc.liamg@":
        print("please enter valid gmail")
        gmail= input("at this moment we only supprot gmail. please enter your gmail")
        b=gmail[::-1]
        c=b[:10]

    passw=input("Please create new password.at the end of it include some sort of symbol")
    b=passw[::-1]
    d=b[:1]
    while d not in ["!","@","#","$","%","^","&","*"]:
        passw=input("Please create new password.at the end of it include some sort of symbol")
        b=passw[::-1]
        c=b[:1]
    rpassw=input("re-enter your password")
    while rpassw != passw:
        rpassw=input("re-enter your password")

while True:
    print("would you like to buy something?")
    a= input("")
    while a not in ["yes","no"]:
        print("please answer yes or no")
        a= input("")
    if a == "yes":
        print("what is your product of choice")
        answer= input("")
        while answer not in computer_parts:
            print("we dont have it right now")
            print(f"her i s what we have rn {computer_parts}")
            print("what is your product of choice")
            answer= input("")
        price=price+int(prices[computer_parts.index(answer)])
        print(price)
        bucket_list.append(answer)
        print(f"you have {len(bucket_list)} items in your bucket list")
    else:
        print("would you like to exit?")
        a= input("")
        while a not in ["yes","no"]:
            print("please answer yes or no")
            a= input("")
        if a == "yes":
            print("would you like to cashout or leave?")
            ans= input("")
            while ans not in ["cashout", "leave"]:
                print("answer with 'cashout' or 'leave'")
                print("would you like to cashout or leave?")
                ans= input("")
            if ans =="cashout":
                while c !="moc.liamg@":
                    print("you have to register first to cashout sir!")
                    gmail= input("at this moment we only supprot gmail. please enter your gmail")
                    b=gmail[::-1]
                    c=b[:10]
                    while c !="moc.liamg@":
                        print("please enter valid gmail")
                        gmail= input("at this moment we only supprot gmail. please enter your gmail")
                        b=gmail[::-1]
                        c=b[:10]

                    passw=input("Please create new password.at the end of it include some sort of symbol")
                    b=passw[::-1]
                    d=b[:1]
                    while d not in ["!","@","#","$","%","^","&","*"]:
                        passw=input("Please create new password.at the end of it include some sort of symbol")
                        b=passw[::-1]
                        c=b[:1]
                        rpassw=input("re-enter your password")
                    while rpassw != passw:
                        rpassw=input("re-enter your password")
                
            
                print("here is your bucket list")
                print(bucket_list)
                print(f"your total will be - {price}")
                card_number=int(input("input card number"))
                cvc= int(input("input your cvc"))
                exp_date= int(input("input your exparation date"))
                print("confirm?")
                answerr= input("")
                if answerr=="yes" or answerr=="y":
                    print("thanks for shopping with us")
                print("BYE")
                break
            else:
                print("BYE")
                break
