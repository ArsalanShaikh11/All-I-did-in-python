n=int(input("enter a number"))

sum=sum(int(digit) for digit in str(n))

result = n% sum==0

if(result):
    print("yes is niven")
    
else:
    print("no is not niven")