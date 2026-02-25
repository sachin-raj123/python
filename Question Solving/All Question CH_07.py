  #  ch - 07 (Topic - file I/O in python, open read & close file , character, reading a file writing to a file, with syntax, deleting a file.)

      # CH - 07 (Topic - file handling)

#QO. 01 WAP to create a file and write some data into it.

# f = open("D:\Python\Question Solving\demo.txt", "r")

# data = f.read()
# print(data)
# print(type(data))
# f.close()

#QO. 02 WAP to create a file in code and write & append some data into it.

# f = open("simple.txt", "a")
# # f.write("hy i am learning java")
# f.write("\nI am learning python")

# f.close()

#QO. 03 create anew file "practice.txt" using python. add the following data in it.

# f = open("practice.txt", "w")

# f.write("hi everyone. \nwe are learning file I/O." )
# f.write("\nusing java. \ni like programing in java.")
# f.close()

#QO. 04 WAP that replace all acurrences of word "java" with "python" in the file "practice.txt".

# f = open("practice.txt", "r")
# data = f.read()
# new_data = data.replace("java", "python")
# print(new_data)

# f = open("practice.txt", "w")
# f.write(new_data)
# f.close()

#QO. 05 search if the word "learning" is present in the file "practice.txt" or not.

# word = "learning"

# with open("practice.txt", "r") as f:
#     data = f.read()

#     if(data.find(word) != -1):
#         print("Found")

#     else:
#         print("Not Found")

#QO. 06 WAF to find in which line of the file does the word "learning" occurs first.
              # print -1 if word is not found.

# def check_for_word():
#      word = "learning"
#      with open("practice.txt", "r") as f:
#         data = f.read()
#         if(word in data):
#             print("Found")
#         else:
#             print("Not Found")

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1

#     return -1   
# print(check_for_line())    

#QO. 07 WAP to create a file and write a string into a it using open() and write() method.

# f = open("simple.txt", "w")
# f.write("hi everyone. \nI am learning file handling in python.")

# f.close()

#QO. 08 WAP to open a file in read mode and display its context.

# with open("simple.txt", "r") as f:
#     data = f.read()
#     print(data)

#QO. 09 Write a program to count the number of characters in a file.

# with open("simple.txt", "r") as f:
#     data = f.read()
#     count = len(data)
#     print("total character:", count)

#QO. 10 Write a program to read only the first 10 characters from a file.

# with open("simple.txt", "r") as f:
#     data = f.read(10)
#     print(data)

#QO. 11 Write a program to append new content to an existing file.

# with open("simple.txt", "a") as f:
#     f.write("\nI am from india.")

#QO. 12 Write a program to read a file line by line using a loop.

# with open("simple.txt", "r") as f:
#     for line in f:
#         print(line, end="")

#QO. 13 Write a program to copy the content of one file into another file.

with open("simple.txt", "r") as source:
    data = source.read()

with open("copy.txt", "w") as target:
    target.write(data)

print("Content copied successfully!")
