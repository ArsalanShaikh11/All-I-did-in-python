#dictionary contains keys and values together they are item

d1={"Name" : "arsalan",
    "Age" : 12,
    "Std" : "se"}

for k,v in d1.items():
    print(k,v)
    
for k in d1.keys():
    print(k)
    
for v in d1.values():
    print(v)
    
d1["Name"]="Arsalan"
print(d1)

d1["Name1"]="Shaikh"
print(d1)


del(d1["Name1"])
print(d1)

    