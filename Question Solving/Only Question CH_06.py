#     ch - 06 (Topic -function in python, types of function, default parameters, recursion.)

#QO. 01 caculate average of 3 number. 

# def calc_avg(a , b, c):
#     sum = a + b + c

#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(50, 87, 92)

#QO. 02 WAF to print the length of a list (list in the parameter)

# num =[12, 15, 17, 20, 22, 25]

# cities =["dehli", "patna", "mumbai", "chenni", "pune"]

# def print_len(list):
#     print(len(list))

# print_len(num)
# print_len(cities)

#QO. 03 WAF to print the element of a list in a single line(list is the parameter).

# cities = ["delhi", "patna", "mumbai", "chennai", "pune"]
# heroes = ["thor", "ironman", "captain america"]

# def print_list(lst):
#     for item in lst:
#         print(item, end=" ")
#     print()   # new line after printing

# print_list(cities)
# print_list(heroes)

#QO. 04 WAF to find the factorial of n . (n is the parameter).

# def cal_fact(n):
#     fact = 1
#     for i in range(1 , n+1):
#         fact *= i
#     print(fact)

# cal_fact(8)

#QO. 05 WAF to convert USD to INR . 

# def convertor(usd_val):
#     inr_val = usd_val * 90

#     print(usd_val, "USD =" , inr_val, "INR")    

# convertor(121)

#QO. 06

# num = int(input("enter a number :"))

# def cal_function(num):
#     if(num % 2 == 0):
#         print("EVEN")
#     else:
#         print("ODD")


# cal_function(num)       

#QO. 07 write a recursive funtion to calculate the sum of first n natural number . 

# def calc_sum (n):
#     if(n == 0):
#         return 0
    
#     return calc_sum(n-1) + n
# sum = calc_sum (10)
# print(sum)

#QO.08 Write a program to create a simple function that prints "Hello, World!".

# def print_hello():
#     print("hello, world!")

# print_hello()

#QO. 09 Write a function that takes a number as a parameter and prints its square.

# def cal_num(n):
    
#     print(n * n)
# cal_num(98)    

#QO. 10 Write a function that takes two numbers as arguments and returns their sum.

# def cal_sum(a , b):

#     sum = a + b
#     print(sum)

#     return sum
# cal_sum(10, 20)

#QO. 11 Write a function with a default parameter that prints a greeting message.
          #(Example: Hello, Guest if no name is given.)

def greet(name = "Guest"):
    print("hello" , name)

greet("sachin")
greet()

#QO. 12 Write a function to check whether a number is even or odd.

num = int(input("enter a number :"))

def cal_func(num):
    if(num % 2 == 0):
        print("EVEN")
    else:
        print("ODD")

cal_func(num)

#QO. 13 Write a function that takes a list as input and returns the maximum element.

def cal_max(numbers):
    maximum = numbers[0]

    for num in numbers :
        if num > max:

            maximum = num

        return maximum    
numbers = list(map(int,input("enter number separated by space:").split()))

result = cal_max(numbers)
print("maximum element is:", result)
 
#QO. 14 Write a function to calculate the factorial of a number using a loop.

def cal_fact(n):
    fact = 1

    for i in range(1,n+1):

     fact *= i
    print(fact)

cal_fact(8)

