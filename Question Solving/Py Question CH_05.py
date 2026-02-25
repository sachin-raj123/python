   # CH - 05 Loop (topic-)

#QO. 01 print number from 1 to 100.

# num = 1
# while num <= 100:
#     print(num)

#     num += 1
# print("loop ended")    

#QO. 02 print number from 100 to 1.

# i = 100
# while i >= 1:
#     print(i)

#     i -= 1
# print("loop ended")

#QO. 03 print the multiplication table of a number n.

# n = int(input("enter number :"))
# i = 1 
# while i <= 10:
#      print(n*i)
#      i += 1

#QO. 04 print the elements of the following list using a loop.
      #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])

#     idx += 1

#QO. 05

# heros = ["batman", "Ironman", "Spiderman", "thor"]

# idx = 0
# while idx < len(heros):
#     print(heros[idx])

#     idx += 1

#QO. 06 search for a number x in this tuple using loop.
   #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found at idx", i)
#     else :
#         print("finding...")

#     i += 1

#QO. 07 print the element of the following list using a loop .

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for val in nums:
#     print(val)

#QO. 08 search for a number x in this tuple using loop . 

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 49

# idx = 0
# for val in tup :
#     if(val == x):
#         print("number found at idx" , idx)

#     idx += 1

#QO. 09 print numbers from 1 to 100. using for & range().

# for val in range(1 , 101):
#     print(val)

#QO. 10 print numbars from 100 to 1 . using for & range()

# for val in range(100 , 0, -1):
#     print(val)

#QO. 11 print a multiplication table of a number n .

     # method 01
# for num in range(3 , 31, 3):
#     print(num)

     # method 02
# n = int(input("enter number :"))

# for i in range(1, 11):
#     print(n * i)

#QO. 12 WAP to find the sum of first n numbers . (using while)

# n = 5

# sum = 0 
# for val in range(1,n+1):
#     sum += val

# print("total sum of val =", sum)    

#QO. 13 WAP  to print number from 1 to 10 using a for loop .

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for val in n :
#     print(val)

#QO. 14 Write a program to print even numbers between 1 and 20 using the range() function.

# for nums in range(2, 21, 2):
#     print(nums)

#QO. 15 Write a program to find the sum of the first n natural numbers using a while loop.

# n = 817
# sum = 0
# i = 1
# while i <= n :
    
#    sum += i
#    i += 1
   
# print("sum of first", n , "natural number =", sum)

#QO. 16 Write a program to print the multiplication table of a given number using a for loop.

# n = int(input("enter a number: "))

# for val in range(1,11):
#     print(n * val)

#QO. 17 Write a program to count the number of digits in a number using a while loop.

# num = int(input("enter a number:"))

# count = 0
# while num > 0:
#     num = num // 10

#     count += 1

# print("total digit =", count)

#QO. 18 Write a program to print numbers from 1 to 50, but stop the loop if the number is divisible by 7 (use break).

# i = 1 

# while i <= 50:
#     print(i)

#     if (i % 7 == 0):
#      break
    
#     i += 1
# print("end the loop")    
    
#QO . 19 Write a program to print numbers from 1 to 20, but skip numbers that are divisible by 3 (use continue).

# i = 1

# while i <= 20:

#     if (i % 3 == 0):
#         i += 1
#         continue
    
#     print(i)
#     i += 1
# print("end the loop")

#QO. 20 Write a program to reverse a number using a while loop.

num = int(input("enter a number :"))
reverse = 0

while num >0:
    digit = num % 10

    reverse = reverse * 10 + digit
    num = num // 10

print("reverse number =" , reverse)    


#QO. 21 Write a program to print a pattern using nested for loops. 
"""
Example:
*
**
***
****

"""

for i in range(1 , 5):
    
    for j in range(1 , i+1):
     print("*" , end = "")

    print()

