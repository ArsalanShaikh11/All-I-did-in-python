contact={"Help":100,
         "Arsalan":12121213}

dict={}

def add_contact(name,number):
    if name in contact:
        print("Contact already exits")
    else:
        contact[name]=number
        print(" added to contacts list" )
        
def Search_contact(name):
    if name in contact:
        print("your contact is ",name,contact[name])
    else:
        print("No such number exist")
        
def delete_contact(name):
    if name in contact:
        del contact[name]
        print("deleted successfullu")
    else:
        print("no data")
        
def updatecontact(name,number):
    if name in contact:
        contact[name]=number  
        print("updated")      
    else:
            print("no suct contact")
            
def displaycontact():
    print("contacts are")
    for k,v in contact.items():
        print(k,"->",v)
            
def favouritecontact(name,number):
   
    if name in contact:
        print("contact alreaddy exits")
    else:
        dict[name]=number
        
def Display_favourit():
    print("favourite contact is")
    for k , v in dict.items():
        print(k,"->",v)
        

    
favouritecontact("Arsalan",12121212)

print("1-Add Contact\n2-Search Contact\n3-DeleteContact\n4-update Contact\n5-Display Contact\n6-Display favourite\n7-Exit\n8-ADD favourite")

while True:
    choice=int (input ("Enter your choce(1/2/3/4/5/6/7/8)"))
    if choice==1:
        name=input ("Enter your name:")
        number=int (input("Enter your number: "))
        add_contact(name, number)
    elif choice==2:
        name = input ("1 Enter your name: ")
        Search_contact(name)
    elif choice ==3:
        name =input("Enter your name: ")
        delete_contact(name)
    elif choice==4:
        name = input ("Enter your name: ")
        number = (input ("Enter your number:"))
        updatecontact (name, number)
    elif choice==8:
        name = input ("Enter your name: ")
        number = (input ("Enter your number:"))
        favouritecontact(name,number)
    elif choice == 5:
        displaycontact()
    elif choice==6:
        Display_favourit()
    elif choice== 7:
        print("Exit")
        break
    else:
      print ("Invalid input")
      