import random as rd

computer = rd.randint(1,20)

print("Enter your name")
name=input()

print("OK", name,"lets strt")

chances = 5

while chances>=1:
    choice =int(input("Enter yur guess"))
    
    if choice>computer:
        print("guess is higher")
        
    elif choice<computer:
        print("lower")
        
    elif choice == computer:
        break
    
    chance = computer-1
    
    
if choice == computer:
    print("you won the game")
    
else:
    print ("You lost the game. The number was ")