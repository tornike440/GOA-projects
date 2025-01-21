#8) შექმენით shopping სია სადაც მომხმარებელს შეეძლება რამე ნებისმიერი პროუქტის
#  დამატება და წაშლა, როდესაც მორჩებიან შოპინგს დაუპრინტეთ საბოლოოდ რა შეიძინეს 
print("hi welcome to out online groceries shop")
bucket=[]
groceries = [
    "milk", "eggs", "bread", "chicken", "apples", "bananas", "potatoes", "carrots", "onions", "tomatoes",
    "cheese", "yogurt", "butter", "rice", "pasta", "flour", "sugar", "salt", "pepper", "garlic",
    "bell peppers", "lettuce", "cucumbers", "broccoli", "cauliflower", "zucchini", "spinach", "kale",
    "oranges", "grapes", "strawberries", "blueberries", "raspberries", "peanut butter", "jam", "honey",
    "coffee", "tea", "orange juice", "apple juice", "cereal", "oatmeal", "granola bars", "potato chips",
    "tortilla chips", "salsa", "pretzels", "popcorn", "frozen pizza", "ice cream", "frozen vegetables",
    "frozen fruit", "frozen waffles", "frozen meals", "ground beef", "steak", "pork chops", "bacon",
    "sausages", "hot dogs", "ham", "turkey", "canned tuna", "canned chicken", "canned beans", "canned soup",
    "canned tomatoes", "canned corn", "canned green beans", "canned peas", "ketchup", "mayonnaise",
    "mustard", "salad dressing", "soy sauce", "vinegar", "olive oil", "vegetable oil", "baking powder",
    "baking soda", "chocolate chips", "vanilla extract", "brown sugar", "powdered sugar", "evaporated milk",
    "condensed milk", "bagels", "muffins", "english muffins", "tortillas", "crackers", "chewing gum",
    "cookies", "candy bars", "nuts", "seeds", "trail mix", "water bottles", "sparkling water", "soda",
    "energy drinks", "sports drinks", "wine", "beer", "liquor", "toilet paper", "paper towels", "napkins",
    "aluminum foil", "plastic wrap", "zipper bags", "laundry detergent", "dish soap", "sponges",
    "cleaning sprays", "trash bags", "shampoo", "conditioner", "body wash", "soap bars", "toothpaste",
    "toothbrushes", "floss", "deodorant", "razors", "shaving cream", "lotion", "baby food", "diapers",
    "wipes", "cat food", "dog food", "bird seed", "cat litter", "dog treats", "herbs", "spices",
    "ginger", "cilantro", "parsley", "basil", "oregano", "thyme", "rosemary", "green onions",
    "avocado", "mangoes", "pears", "pineapple", "watermelon", "cantaloupe", "kiwi", "plums",
    "cherries", "blackberries", "figs", "pomegranates", "sweet potatoes", "turnips", "beets",
    "brussels sprouts", "artichokes", "asparagus", "mushrooms", "celery", "eggplant", "radishes",
    "parsnips", "leeks", "squash", "peaches", "nectarines", "apricots", "dates", "lemons", "limes",
    "grapefruit", "pumpkin", "cabbage", "bok choy", "okra", "edamame", "peas", "lentils", "quinoa",
    "couscous", "barley", "almond milk", "soy milk", "coconut milk", "tofu", "tempeh", "veggie burgers",
    "plant-based meats", "sunflower oil", "sesame oil", "coconut oil", "cornmeal", "bread crumbs",
    "pancake mix", "waffle mix", "syrup", "hot sauce", "barbecue sauce", "pasta sauce", "pickles",
    "olives", "capers", "anchovies", "fish sticks", "shrimp", "salmon", "tilapia", "crab", "lobster",
    "scallops", "clams", "cod", "haddock", "mussels", "oysters", "whipping cream", "cream cheese",
    "sour cream", "cottage cheese", "whipped cream", "mozzarella sticks", "string cheese"
]

while True:
    print("would you like to buy something?")
    a= input("")
    while a not in ["yes","no"]:
        print("please answer yes or no")
        a= input("")
    if a == "yes":
        print("what is your product of choice")
        answer= input("")
        while answer not in groceries:
            print("unfortunalty we dont have it right now: here is what we have at the moment, please choose from this")
            print(groceries)
            print("what is your product of choice")
            answer= input("")
        bucket.append(answer)
        print(f"added'{answer}' in the bucket list")
    else:
        print("would you like to cashout or leave?")
        ans= input("")
        while ans not in ["cashout", "leave"]:
            print("answer with 'cashout' or 'leave'")
            print("would you like to cashout or leave?")
            ans= input("")
        if ans =="leave":
            print("BYE")
            break
        else:
            print("here is your bucket list")
            print(bucket)
            card_number=int(input("input card number"))
            cvc= int(input("input your cvc"))
            exp_date= int(input("input your exparation date"))
            print("confirm?")
            answerr= input("")
            if answerr=="yes" or answerr=="y":
                print("thanks for shopping with us")
            print("BYE")
            break


