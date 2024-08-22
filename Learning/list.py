friend = [1,2,3,4,5,6]
print(type(friend))
print (friend)

for f in friend:
    print(f)
    
friend.append(7)
friend.remove(2)
print (friend)
print (friend.pop())
print (friend.count(5))
friend.insert(1,111)
print (friend)


copylist = friend.copy
friend.clear
print(copylist)
#delete_friend
print (friend)

if 5 in friend:
    print ("5 is in the list")
    
if 333 not in friend:
    print ("333 is not in the list")

    