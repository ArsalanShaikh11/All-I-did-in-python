#Changing last and first element in the list
'''
list = [7,2,3,4,5,6,1]
print(list)
size=len(list)
temp=list[0]
list[0]=list[size-1]
list[size-1]=temp
print(list)
'''
#length of string
'''
str="hello worrrld"
s=len(str)
print(s)
'''
#max and min of two number
'''
a=10
b=20
if a>b:
    print("a is gretaer")
else:
    print("b is greater")
if a<b:
    print("a is smaller")
else:
    print("b is smaller")
'''
#Check element exist in list
'''
list=[1,2,3,4,5,6,7,8]
element=int(input("Enter the element to verify:-"))
if element in list:
    print("Element exists in the list")
else:
    print("Element does not exists in the list")
'''
#way to clear a list in python
'''
list=[1,2,3,4,5,6,7]
#list.clear()
#list*=0
#del list[:]
#while len(list)!=0:
    #list.pop()
list=list[:0]
print(list)
'''
#copy a list
'''
list=[1,2,3,4,5,5,6,7]
a=list.copy()
print(a)
'''
#reversing a list
'''
l=[1,2,3,4,56,7,8]
#l.reverse()
l=l[::-1]
print(l)
'''
#avg of string 
'''
l=[1,2,3,4,5,6,7]
leng=len(l)
print(leng)
A=0
for i in l:
    A=A+i
c=A/leng
print(c)
'''
#multiply
'''
l=[1,2,3,4,5,6,7]
product=1
for i in l:
    product=product*i
print(product)
'''
#count number of element repeaated
'''
l=[1,2,3,4,5,6,7,1,1]
print(l.count(1))
'''
#smllest and largest int the list
'''
l=[1,2,3,4,5,6,7,1,1]
#print(min(l))
#print(max(l))
l.sort()
print(l[0])
l.sort(reverse=True)
print(l[0])
'''
#even number and odd
'''
l=[1,2,3,4,5,6,7,1,1]
#for  i in l:
 #   if i%2==0:
  #      print(i)
for i in l:
    if i%2 != 0:
        print(i)
'''
#even and odd number in range
'''
l=[1,2,3,4,5,6,7,1,1]
#for i in range(1,5):
 #   if i%2 == 0:
   #     print(i)
for i in range(1,6):
    if i%2 != 0:
        print(i)
'''
#count even and odd
'''
l=[1,2,3,4,5,6,7,1,1]
even,odd=0,0
for i in l:
    if i%2 == 0:
        even+=1
    else:
        odd+=1
print(even,odd)
'''
#count positive nd negative number
'''
l=[1,2,3,4,5,6,-7,-1,-1]
pos,nega=0,0
for i in l:
    if i>0:
        pos+=1
    else:
        nega+=1
print(pos,nega)
'''
#pos and nega number
'''
l=[1,2,3,4,5,6,-7,-1,-1]
for i in l:
    if i>0:
        print(i)
'''
#finding dublicate
'''
l=[1,2,3,4,5,6,-7,-1,-1]
dublicate=[]
for i in l:
    if i not in dublicate:
        dublicate.append(i)
print(dublicate)
'''
