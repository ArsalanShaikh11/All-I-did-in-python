num=int(input("Enter any Number : "))
sum=0
product=1
temp=num
while num>0:
    digit=num%10
    sum=sum+digit
    product=product*digit
    num=num//10
if (product+sum)==temp:
    print("it is Special Number ")
else:
    print("it is not a Special Number ")