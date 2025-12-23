                # Practice Questions No. 01

# name = input("Enter your name: ")
# print("lenght of your name is:", len(name))

                # Practice Questions No. 02

# str = "Hi, $Iam sachin the $ is symbol of $99.9 and $ is used"
# print(str.count("$"))

                # Practice Questions No. 03

# num = int(input("enter number : "))

# if(num % 2 == 0):
#     print("EVEN")
# else:
#     print("ODD")

                # Practice Questions No. 04

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if(a >= b and a >= c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("third number is largest", c)


a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))

if(a >= b and a >= c and a >= d):
    print("first number is largest", a)
elif(b >= c and b >= d):
    print("second number is largest", b)
elif(c >= d):
    print("third number is largest", c)
else:
    print("fourth number is largest", d)

