def isHappyNumber(n):    
    digit = sum = 0    
    while(n > 0):    
        digit = n % 10 
        sum = sum + (digit * digit)    
        n = n // 10   
    return sum    
        
num = int(input("Enter a number: "))    
result = num    
     
while(result != 1 and result != 4):    
    result = isHappyNumber(result)      
if(result == 1):    
    print(num, " is a Happy Number")   
else:    
    print(num, " is an not an happy Number")