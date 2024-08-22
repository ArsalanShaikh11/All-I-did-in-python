import random as r
chance =5
Com=0
User=0
while chance>=1:
    computer =r.choice(["Head","Tail"])
    choice=input("Enter your choice")
    if choice==computer:
        print("you won")
        User=User+1
    elif choice=="Head":
        if computer== "Tail":
            print("coin has Tail")
            Com =Com+1
        else:
            print("coin has Head")
            Com=Com+1
    else:
        print("correct choice")
        
    chance=chance-1
    print("Computer",Com)
    print("User",User)

if Com>User:
    print("BAAP se khelega laude")
else:
    print("Kal aana mmuh dhoke jh2")
    