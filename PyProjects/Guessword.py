c=("a","c","m","p","s","t")
l=["mat","man","can","cat","cap","camp"]
repeat=[]
name=input("Enter your name:-")
chance=5
while chance>=1:
    
    print("make a word for the following alphabets")
    print(c)
    choice=input("Enter a noun of 3 or more letter from the above list:-")
    
    if len(choice)>=3:
        if choice in l:
            print("your choice is correct:-",choice)
            l.remove(choice)
            repeat.append(choice)
        elif choice in repeat:
            print("you have already chosen this one,please choose another one.")
            chance+=1
        else:
            print("wrong choice please enter again")
            chance+=1
    else:
        print("invalid input please enter again with at least three letters")
    chance-=1
    
            