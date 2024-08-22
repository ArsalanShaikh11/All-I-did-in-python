import pandas as pd

# x=pd.Series(["name","age","address"],index=["a","b","c"])
# print(x)
# print(x["a"])

y=pd.DataFrame({"name": ["Arsalan","Nadeem","Hanzu"],
               "age":[20,14,14],
               "ADD":[30,30,30]})

print(y)
#works same as dictionary
print(y["age"].describe())
print(y["age"].min())
print(y["age"].max())

y["age"][0]=20
print(y)