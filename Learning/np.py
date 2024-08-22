import numpy as np 

a = np.array(45)
print(a)
print(a.ndim)
print("\n")
print(a)


a = np.array([45, 55])
print(a)
print(a.ndim)
print("\n")
for i in a:
    print(i)

a = np.array([[45, 55], [65,75]])
print(a)
print(a.ndim)
print("\n")
for i in a:
    for j in i:
        print(j)


a = np.array([[[45,55], [65,75]], [[85,95],[25,35]]])
print(a)
print(a.ndim)
print("\n")
for i in a:
    for j in i:
      for k in j: 
         print(k)



a = np.array([[[[15,25],[35,45]], [[55,65],[75,85]]], [[[95,96],[97,98]],[[99,89],[88,87]]]])
print(a)
print(a.ndim)
print("\n")
for i in a:
    for j in i:
      for k in j: 
         for l in k:
              print(l)


a = np.array([[[[[1,2],[3,4]],[[5,6],[7,8]]], [[[9,10],[11,12]],[[13,14],[15,16]]]], [[[[17,18],[19,20]],[[21,22],[23,24]]],[[[25,26],[27,28]],[[29,30],[31,32]]]]])
print(a)
print(a.ndim)
print("\n")
for i in a:
    for j in i:
      for k in j: 
         for l in k:
              for m in l:
                print(m)