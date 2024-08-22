# print("Enter three numbers: ")
# n1=int(input())
# n2=int(input())
# n3=int(input())
# if n1>n2 and n1>n3:
#     print("Largest number is",n1)
# elif n2>n1 and n2>n3:
#     print("Largest number is",n2)
# else:
#     print("Largest number is",n3)



# list=["Arsalan","Ali","Asif","Ali","Salman","Asif"]
# dublicate_list=[]

# for i in list:
#     if i not in dublicate_list:
#         dublicate_list.append(i)
# print("The list is",dublicate_list)


# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("Fizzbuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)



# rows=6
# for i in range(1,6):
#     for j in range(i):
#         print("*", end=' ')
#     print('')



# num=int(input("Enter the number for multiplycation: "))

# for i in range(1,11):
#     print(f"{num} x {i} = {i*num}")



# Vowel=["a","e","i","o","u","A","E","I","O","U"]
# count=0
# char=input("Enter a string:")

# for i in char:
#     if i in Vowel:
#         count=count+1
# print(f"Total number of Vowels are :{count}")



# Weight=int(input("Enter your weight:-"))
# unit=input("lbs or kg:-")

# if unit=="lbs":
#     Weight=Weight*0.4536
#     print("Your weight is",Weight,"kg")
# elif unit=="kg":
#     Weight=Weight/0.4536
#     print(f"Your weight is {Weight} lbs")
    


# sample_string = "Hello, World!"
# print("1. Length of the string:", len(sample_string))
# print("2. Lowercase:", sample_string.lower())
# print("3. Uppercase:", sample_string.upper())
# print("4. Capitalized:", sample_string.capitalize())
# print("5. Count of 'l':", sample_string.count('l'))
# print("6. Index of 'World':", sample_string.find('World'))
# print("7. Replace 'Hello' with 'Hi':", sample_string.replace('Hello', 'Hi'))
# print("8. Split at comma:", sample_string.split(','))
# whitespace_string = "    Hello, World!    "
# print("9. Stripped string:", whitespace_string.strip())
# print("10. Is the string alphabetic?", sample_string.isalpha())



# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print("1. Length of set1:", len(set1))
# set1.add(6)
# print("2. After adding 6 to set1:", set1)
# set1.remove(3)
# print("3. After removing 3 from set1:", set1)
# popped_element = set1.pop()
# print("4. Popped element from set1:", popped_element)
# set1.clear()
# print("5. After clearing set1:", set1)
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print("6. Intersection of set1 and set2:", set1.intersection(set2))
# print("7. Union of set1 and set2:", set1.union(set2))
# print("8. Difference of set1 and set2:", set1.difference(set2))
# print("9. Symmetric difference of set1 and set2:", set1.symmetric_difference(set2))
# print("10. Are set1 and set2 disjoint?", set1.isdisjoint(set2))    



# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# print("1. Length of the dictionary:", len(my_dict))
# print("2. Keys in the dictionary:", my_dict.keys())
# print("3. Values in the dictionary:", my_dict.values())
# print("4. Items in the dictionary:", my_dict.items())
# print("5. Value associated with 'b':", my_dict.get('b'))
# removed_value = my_dict.pop('c')
# print("6. Removed value associated with 'c':", removed_value)
# print("Dictionary after pop operation:", my_dict)



# sample_string = "Hello, World!"
# tuple_from_string = tuple(sample_string)

# print("Tuple from string:", tuple_from_string)



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# student1 = Student("Alice", 20)
# student2 = Student("Bob", 22)
# student3 = Student("Charlie", 21)
# print("Student 1:")
# print("Name:", student1.name)
# print("Age:", student1.age)
# print()
# print("Student 2:")
# print("Name:", student2.name)
# print("Age:", student2.age)
# print()
# print("Student 3:")
# print("Name:", student3.name)
# print("Age:", student3.age)



# filename = '1.txt'
# def count_file_stats(filename):
#     num_lines = 0
#     num_words = 0
#     num_chars = 0

#     with open(filename, 'r') as file:
#         for line in file:
#             num_lines += 1
#             num_words += len(line.split())
#             num_chars += len(line)
#     return num_lines, num_words, num_chars
# num_lines, num_words, num_chars = count_file_stats(filename)

# print("Number of lines:", num_lines)
# print("Number of words:", num_words)
# print("Number of characters:", num_chars)



# append()
# extend()
# insert()
# remove()
# pop()
# index()
# count()
# sort()
# reverse()
# clear()