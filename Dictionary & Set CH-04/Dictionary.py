                # Dictionary in Python #

# dict = {}   # empty dictionary

# dict = {
#     "key" : "value",
#     "name" : "sachin",
#     "cgpa" : 9.1,
#     "learning" : "Python",
#     "collage" : "apnacollage",
#     "age" : 21

# }

# print(dict["key"])
# print(dict["name"])
# print(dict["cgpa"])
# print(dict["learning"])
# print(dict["age"])
# print(dict["collage"])

                 # Nested Dictionary  # 

# student = {
#     "name" : "sachin",
#     "subjects" : {
#         "science" : 85,
#         "maths" : 90,
#         "english" : 88
#     }
# }

# print(student)
# print(student["subjects"])
# print(student["subjects"]["maths"])


    #keys Method
# print(list(student.keys()))
# print(type(student))


    #values Method
# print(list(student.values()))


    #items Method
# print(list(student.items()))
# pairs = list(student.items())
# print(pairs[0])


    # get "key" Method
# print(student("name"))     #error
# print(student.get("name"))   #no  error --> None


    #update Method
# student.update({"city": "delhi"})

# print(student)
