#wap to print fibonacci series up to hundred using function
def fibonacci():    
    n1=0
    n2=1
    sum=n1+n2
    print(n1)
    print(n2)
    while sum<=100:
        n1=n2
        n2=sum
        print(sum)
        sum=n1+n2
fibonacci()   

#wap to find the factorial of a given no using function
def find_factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact = fact*i
        i=i+1
        
    print("factorial is",fact)    
find_factorial(5)
        
#wap to pass a list to a fuction and print the sum of the list   
A=[1,2,3,4,5,6,7,8,9]
def find_sum():
    sum=0
    for i in A:
        sum=sum+i  
    print(sum)   
find_sum()    
     
#wap to pass a list to a functin reverse the list manually and return the reverse list 
Ars=[1,2,3,4,5,6,7,8,9]     
def reversing(Ars):
    rev =Ars[::-1]
    print(rev)
reversing(Ars)    

#wap to build a calculator(if else ladder)   
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculate(x, y, operator):
    if operator == '+':
        return add(x, y)
    elif operator == '-':
        
        return subtract(x, y)
    elif operator == '*':
        return multiply(x, y)
    elif operator == '/':
        return divide(x, y)
    else:
        return "Invalid operator"

print(calculate(5, 2, '+'))
print(calculate(5, 2, '-'))
print(calculate(5, 2, '*'))
print(calculate(5, 2, '/'))