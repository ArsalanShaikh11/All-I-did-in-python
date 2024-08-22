
#sum of a list
list=[[1,2,3],[4,5,6],[7,8,9]]
sum = 0

for outer in list:
    for inner in outer:
        sum=sum+inner
        
print(sum)



#create a list of numbers annd check how many are prime no
ARS=[1,2,5,153,233]

count =0

for i in ARS:
    temp = i
    rem=0
    sum=0
    while i>0:
        rem = i%10
        su=sum +(rem**3)
        num=num//10
    if(temp==sum):
        print(temp,"it is armstrong")
        count = count +1
        
print("total armsrong",count)    
    
        
        
    

    


