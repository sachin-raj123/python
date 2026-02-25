
#  ch - 02 (Topic -strings, basic operation, indexing, slicing negative, index, string function, conditional statement)

#           Qo. of   Strings    CH - 02 

# QO. 1   WAP to input user's name & print its length.

# name = input("enter your name: ")

# print(len(name))


# QO. 2 WAP to find the occurrence of '$' in a string.

# str = "hi, $ is my name $t am $symbol of dollar$"

# print(str.count('$'))


# QO. 3 WAP to find the occurrence of is in a string.

# str = " hi is a collage is located in city is a beautiful is and the end"

# print(str.count('is'))


#                conditional Statements

# QO. 4 WAP to check if a number entered by the user in odd or evan .             

# num = int(input("enter a number: "))

# if(num % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")


# QO. 05 WAP to find the greatest of 3 numbers entered by the user.

# a =  int(input("enter first number: "))
# b = int(input("enter second number: "))
# c =  int(input("enter third number: "))

# if(a >= b and a >= c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("third number is largest", c)


# QO. 06 WAP to find the greatest of 4 numbers entered by the user.

# a =  int(input("enter first number: "))
# b = int(input("enter second number: "))
# c =  int(input("enter third number: "))
# d =  int(input("enter fourth number: "))

# if(a >= b and a >= c and a >= d):
#     print("first number is largest", a)
# elif(b >= c and b >= d):
#     print("second number is largest", b)
# elif(c >= d):
#     print("third number is largest", c)
# else:
#     print("fourth number is largest", d)


# QO. 07 WAP to check if a number is a multiple of 7 or not. 

# x = int(input("enter a number:"))

# if(x % 7 == 0):
#     print("multiple of 7")
# else:
#     print("not a multiple of 7")    


# QO. 08 WAP to check if a number is a multiple of 8 or not. 

# y = int(input("enter a number:"))              
                                           
# if(y % 8 == 0):                          
#     print("multiple of 8")         
# else:                               
#     print("not a multiple")           


# QO. 09  Write a program to check whether a number is even or odd.

# num = int(input("enter a num :"))

# if (num % 2 == 0):
#     print("EVEN")
# elif(num % 2 != 0):
#     print("ODD")    


# QO. 10 Write a program to input a number and check whether it is positive or negative.

# num = int(input("enter a number :"))

# if (num > 0):
#      print("POSITIVE")

# elif(num < 0):
#     print("NEGATIVE")


# QO. 11  Write a program to find the largest of two numbers

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))

# if (num1 >= num2):
#     print("first number is largest", num1)
# else:
#     print("second number is largest", num2)


# QO. 12 Write a program to input a string and print it.

# user = input("enter your name :")

# print("Welcome :", user)

# QO. 13 Write a program to find the length of a string without using len() function.

# Riya = " hi my name is Riya  Sharma."
  
#   Method 1
# print(len(Riya))

#    Method 2
# count = 0 
# for char in Riya:
#     count += 1

#     print("length of Riya is :", count)

# QO. 14 Write a program to print the first and last character of a string using indexing.

# str = "SACHIN"

# print(str[0],str[5])

# QO. 15 Write a program to print all characters of a string using a loop.

# str = "dehli is a capital of india"

# for char in str:
#     print(char)

# QO. 16 Write a program to print  all input  of a string using a loop.

# str = input("enter your name : ")

# for char in str:
#     print(char)

# QO. 17 Write a program to access characters of a string using positive indexing.

# name = "SACHIN RAJ"

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])

# QO. 18 Write a program to access characters of a string using negative indexing.

# name = "ANKUR"

# print(name[-5])
# print(name[-4])
# print(name[-3])
# print(name[-2])
# print(name[-1])

# QO. 19 Write a program to reverse a string using slicing.

# str = "sachin"
# # Alternative method using slicing
# print(str[::-1])

# QO. 20 Write a program to check whether a string is empty or not.

# str = input("enter your val: ")

# if (str == ""):
#       print("empty string")

# else:
#       print("not empty string")

# QO. 21 Write a program to count the number of vowels in a string

# str = input("enter a values:")

# vowels = 'aeiouAEIOU'
# count = 0 
# for char in str:
#     if char in vowels:
#         count += 1

# print("numbers of vowels :", count)        

# QO. 22 Write a program to check whether a string is a palindrome or not.

# s = input("enter a string: ")

# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# QO. 23 Write a program to convert a string into: (uppercase, lowercase, title case)

# name = input("enter your name: ")

# print("uppercase:", name.upper())
# print("lowercase:", name.lower())
# print("titlecase:", name.title())

# QO. 24 Write a program to replace all spaces in a string with underscore (_).

# str = " i am sachin raj"

# print(str.replace(" ", "_"))

# QO. 25 Write a program to count how many times a character appears in a string.

# val = " delhi is capital of india . delhi is a big city. "

# print(val.count("a"))


