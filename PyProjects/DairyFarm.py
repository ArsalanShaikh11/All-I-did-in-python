customers={}
b=0
m=0
E=0
BU=0
c=0
cc=0
mc=0
wm=0
t=0
bu=0
Customer=input("Are you a customer or visitor:- ")
while Customer=="customer":
    Name=input("Enter your name:- ")
    print("!!!!Available products!!!!")
    print("Bread 22rs\nMilk 50rs\nEggs 30rs\nButter 55rs\nCurd 75rs\nCottage Cheeze 90rs\nMozerella Cheeze 100rs\nWhole Mike 60rs\nTea leaves 40rs\nBuns 60rs")
    chance=int(input("Enter how  many products do you want form the above Available products:-"))
    while chance>=1:
        print("\nWhat you want to buy select according to the choices")
        print("1-Bread 1loaf\n2-Milk 1lt\n3-Eggs 0.5dz\n4-Butter\n5-Curd 1kg\n6-Cottage Cheeze1kg\n7-Mozerella Cheeze 0.5kg")
        print("8-Whole Mike 1lt\n9-Tea leaves 0.5kg\n10-buns 5 piece")
        choice=int(input("Enter product number:- "))
        if choice==1:
            b=b+22
        elif choice==2:
            m=m+50
        elif choice==3:
            E=E+30
        elif choice==4:
            BU=BU+55
        elif choice==5:
            c=c+75
        elif choice==6:
            cc=cc+90
        elif choice==7:
            mc=mc+100
        elif choice==8:
            wm=wm+60
        elif choice==9:
            t=t+40
        elif choice==10:
            bu=bu+60
        else:
            print("Invalid input")
            chance+=1
        chance-=1
    break
    

if Customer=="visitor":
    print("!!!!Available products!!!!")
    print("Bread 22rs\nMilk 50rs\nEggs 30rs\nButter 55rs\nCurd 75rs\nCottage Cheeze 90rs\nMozerella Cheeze 100rs\nWhole Mike 60rs\nTea leaves 40rs\nBuns 60rs")
    print("~~~Thanks for visiting~~~")
    
sum=b+m+E+BU+c+cc+mc+wm+t+bu
if sum==0:
    print("No purchase")
else:
    print("\nSum of your groceries is:-",sum)
    print("Payment can be done via cash or epay")
    print("~~~Thanks for visiting~~~")
    print("       VISIT AGAIN          ")

#customers[Name]=sum
#print(customers)

