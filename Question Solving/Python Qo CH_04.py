  # CH - 04 (topic- Dictionary in pyhton, nested dictionary, dictionary method, set in python, set method)

#QO. 01 store following word meaning in a python dictionary.

# dict = {
 
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture" , "list of facts & figures"]
# }

# print(dict)

#QO. 02 you are given a list of subject for student. assume one classroom is required for 1 subject.
       # How many classroom are needed by all student. 

# set = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

# print(len(set))

#QO. 03 WAP to enter marks of 3 subject form the user and store them in a dictionary .
   # start with an empty dictionary & add one by one . use subject  name as a key & marks of value .

# marks = {}

# x = int(input("enter phy :"))
# marks.update({"phy" : x})

# x = int(input("enter math :"))
# marks.update({"math" : x})

# x = int(input("enter chem :"))
# marks.update({"chem" : x})

# print(marks)

#QO. 04 figure out a way to store 9 & 9.0 as separate value in the set .
 # ( you can take help  of built- in data types)

# values = {9 , "9.0"}
# print(values)

#QO. 05  WAP  to crate a dictionary with student details .
  #(roll no , name , marks ) & print it .

# student = {
    
#     "name" : "sachin raj",
#     "Roll No" : 786,
#     "marks"  : 98

# }

# print(student)

#QO. 06 Write a program to access the value of a dictionary using a key.

# dict = {
#     "name" : "sachin raj"

# }

# print(dict["name"])

#QO. 07 Write a program to add a new key–value pair to an existing dictionary.

#method 01
# student = {
#     "name" : "sachin raj",
#     "Roll no" : 786,
#     "age" : 96
# }

# new_dict = {"city" : "delhi"}

# student.update(new_dict)
# print(student)

#method 02
# student = {
#     "name" : "sachin raj",
#     "Roll no" : 786,
#     "age" : 96
# }

# student.update({"city" : "delhi"})
# print(student)


#QO. 08 Write a program to update the value of an existing key in a dictionary.

# dict = {
#     "name" : "sachin raj",
    
#         "math" : 96.6,
#         "phy" : 98.6,
#         "chem" : 97
#     }

# dict.update ({"chem" : 99})

# print(dict)

#QO. 09 Write a program to delete a key from a dictionary using the pop() method.

# collection = {
#     "city1" : "delhi",
#     "city2" : "patna",
#     "city3" : "jammu"
# }

# collection.pop("city3")

# print(collection)

#QO. 10 Write a program to print all keys and values of a dictionary using a loop.

# collage = {
#     "friend1" : "ankur",
#     "friend2" : "sachin",
#     "friend3" : "satyam",
#     "friend4" : "sagar",
# }

# for key, value in collage.items():
#     print(key, ":", value)

#QO. 11 Write a program to check whether a key exists in a dictionary or not.

# collection = {
#      "name" : "sachin raj",
#     "collage" : "Sviet",
#     "school" : "bihar board"

# }
# print(type(collection))

# if "collage" in collection :
#     print("key exist in dictioary")

# else :
#     print("key does not exist in dictionary")

#QO. 12 Write a program to find the length of a dictionary.

# info = {
#     "name" : "sachin raj",
#     "subject" : ["python", "c", "c++"],
#     "age" : 20,
#     "cgpa" : 98.7,
#     "is_adult" : True
# }

# print(len(info))

#QO. 13 Write a program to create a nested dictionary for student information (name, marks of subjects).

# student = {
#     "name" : "sachin raj",
#     "subject" : {
#         "math" : 98,
#         "phy" : 97,
#         "chem" : 89,
#         "total_marks" : 284
#     }
# }
# print(student)
# print(student["subject"])

#QO. 14 write a program to acess value from a nested dictionary. 

# info = {
#     "surename" : "ankur raj",
#         "collage" : {
#             "network theory" : 54,
#             "analog comm" : 48,
#             "computer system" : 56
#         }
#     }


# print(info["collage"]["analog comm"])
# print(info["collage"]["network theory"])

#QO. 15 Write a program to use dictionary methods: [ keys() ,values(), items() ]

# friends = {
#     "friend1" : "sachin raj",
#     "friend2" : "ankur raj",
#     "friend3" : "satyam raj",
#     "friend4" : "sumit raj",
#     "friend5" : "sagar raj"
# }

#         #key()
# print(list(friends.keys()))

#         #value()
# print(list(friends.values()))

#         #items()
# print(list(friends.items()))

# pairs = list (friends.items())
# print(pairs[1])

#QO. 16 Write a program to create a set and print all its elements.

values = {1, 2, 3, 4, 1, 3,"hello", "world", "world", "delhi", "patna", "delhi", 4}

print(values)
print(type(values))

#QO. 17 Write a program to add and remove elements from a set using add() and remove() methods

collection = set ()

     #add()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add(5)
collection.add(6)
collection.add(7)

print(collection)

     #remove()
collection.remove(1)
print(collection)

