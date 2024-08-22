def passchecker(password):
    upper=False
    lower= False
    digit = False
    symbol=False
    
    if len(password)<8:
        for i in password:
            if i.isupper():
                upper=True
            elif i.islower():
                lower=True
            elif i.isdigit():
                digit= True
            else:
                symbol=True
                
    if  upper and lower and digit and symbol and len(password)<8:
        print("password is strong")
        
    elif upper or lower and digit and symbol and len(password)<8:
        print("moderate password")
    else:
        print("weak password")
        
pass1=input("Enter number")
passchecker(pass1) 