s1={1,2,3,4,5,6}
s2={5,6,7,8,9,0}

c=s2.difference(s1)
print(c)

c=s2.intersection(s1)
print(c)

c=s2.union(s1)
print(c)

c=s2.symmetric_difference(s1)
print(c)

s1.add(10)
print(s1)

s1.discard(10)
print(s1)

c=s2.isdisjoint(s1)

print(c)


