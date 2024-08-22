num=int(input("Enter any Number : "))
sum=0
product=1
while num>0:
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10
 
if(sum==product):
    print(" is a Spy number!")
else:
    print(" is not a Spy number!")
    