'''
try:
    a=int(input("enter number"))
    b=int(input("enter number"))

    c=a+b
    print(c)
except:
    print("Enter number")
'''
    

try:
    a=int(input("enter number"))
    b=int(input("enter number"))

    c=a/b
    print(c)
except ValueError:
    print("Enter number rather than string")
    
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("This is the end of program")



'''
try:
    l=[1,2,3,4,5,6,7]
    a=int(input("enter number"))
    print(1[a])
    
except:
    print(" Enter Valid value")
'''