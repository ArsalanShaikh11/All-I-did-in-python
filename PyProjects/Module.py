import Contact_book as C
from Contact_book import displaycontact

print("1-Add Contact\n2-Search Contact\n3-DeleteContact\n4-update Contact\n5-Display Contact\n6-Exit")

while True:
    choice=int (input ("Enter your choce(1/2/3/4/5/6)"))
    if choice==1:
        name=input ("Enter your name:")
        number=int (input("Enter your number: "))
        C.add_contact(name, number)
    elif choice==2:
        name = input ("1 Enter your name: ")
        C.Search_contact(name)
    elif choice ==3:
        name =input("Enter your name: ")
        C.delete_contact(name)
    elif choice==4:
        name = input ("Enter your name: ")
        number = (input ("Enter your number:"))
        C.updatecontact (name, number)
    elif choice == 5:
        C.displaycontact()
    elif choice== 6:   
        print("Exit")
        break
    else:
      print ("Invalid input")
      
#Any file ending with py is a module and the process of importing the file is known as modularity