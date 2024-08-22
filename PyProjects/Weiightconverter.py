Weight=int(input("Enter your weight:-"))
unit=input("lbs or kg:-")

if unit=="lbs":
    Weight=Weight*0.4536
    print("Your weight is",Weight,"kg")
elif unit=="kg":
    Weight=Weight/0.4536
    print(f"Your weight is {Weight} lbs")
    
    