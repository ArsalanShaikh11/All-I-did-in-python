import random as rd
COM=0
user=0
chance=5


while chance>=1:
    computer =rd.choice(["R","p","s"])
    choice=input("Enter your choice")

    if choice==computer:
        print("its a tie")
        
    elif choice=="R":
        if computer == "P":
                print("you lose",computer)
                COM=COM+1
        else:
            print("yoou win",computer)
            user=user+1
            
    elif choice=="P":
        if computer=="s":
            print("you lose",computer)
            COM=COM+1
        else:
            print("yoou win",computer)
            user=user+1
            
    elif choice=="s":
        if computer=="R":
            print("you lose",computer)
            COM=COM+1
        else:
            print("you win",computer)
            user=user+1
            
    chance =chance-1

print(COM)
print(user)

if COM>user:
    print("BAAP se khelega laude")
else:
    print("Kal aana mmuh dhoke jh2")


        
    
    
