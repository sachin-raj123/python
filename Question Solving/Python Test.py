                                                  # PYTHON TEST ALL QUESTIONS

#QO. 01  Reverse a string without using built-in reverse.

# name  = "sachin raj"

# print(name[::-1])

#QO. 02  Reverse a string without using built-in reverse.

# str1 = "sachin raj"

# rev = ""
# for ch in str1:
#     rev = ch + rev
# print(rev)

#QO. 03 Reverse a string without using built-in reverse.

# name = "sachin raj"

# rev = "" 
# for i in name:
#     rev = i + rev
# print(rev)

#QO. 04 Check if a string is palindrome.

# s = "level"
# if s == s[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#QO. 05 check palindrome without using built-in reverse or slicing.

# s = "madam"
# rev = ""

# for ch in s:
#     rev = ch + rev

# if s == rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#QO. 6 Check if a string is palindrome.

# palimdrome = "level"

# if (palimdrome==palimdrome[::-1]):
#     print("True")

# else:
#     print("False")

#QO. 07 Reverse an integer (e.g., 123 -> 321).

# num = 123

# rev = int(str(num)[::-1])
# print(rev)

#QO. 08 Reverse an integer (e.g., 12345 -> 54321).

# num = 12345

# rev = int(str(num)[::-1])
# print(rev)


#QO. 09 Reverse an float (e.g. 87.65)

# num = 87.65

# rev = float(str(num)[::-1])
# print(rev)

#QO. 10 Check if a number is prime.

# num = int(input("enter a number:"))

# if num <= 1:
#     print("It is not prime number")
# else:
#     for i in range(2, num):
#      if num % i == 0:
#          print("It is not prime number")
#          break
#      else:
#           print("it is a prime")

#QO. 11 Check if a number is prime.

# num = int(input("enter a number :"))

# if num <= 1:
#     print("NOT PRIME")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("NOT PRIME")
#             break
#         else:
#             print("it is prime")

#QO. 12 print all prime number between 1 to n.

# n = int(input("enter a number:"))

# for num in range(2 , n + 1):
#     for i in range(2 , num):
#         if num % i == 0:
#             break
#         else:
#             print(num)

#QO. 13 print all prime number between 1 to n .

# n = int(input("enter a number :"))

# for num in range(2, n+1):
#     for i in range(2, num):
#         if num % i ==0:
#             break
#         else:
#             print(num)

#QO. 14 print all prime number between 1 to n .

# n = int(input("enter a number :"))

# for num in range(2 , n+1):
#     for i in range(2 , num):
#         if num % i == 0:
#             break
#         else:
#             print(num)

#QO. 15 find factorial on a number (iterative).

# num  = int(input("enter a number :"))

# fact = 1 
# for i in range(1 , num + 1):
#     fact = fact * i

#     print("factorial is :", fact)

#QO. 16 find factorial on a number (iterative).

# num = int(input("enter a number:"))

# fact = 1
# for i in range(1 , num + 1):
#     fact = fact * i 

# print("factorial is:", fact)

#QO. 17 find factorial of a number(iterative).

# num = int(input("enter a number:"))

# fact = 1 
# for i in range(1 , num + 1):
#     fact = fact * i

#     print("factorial is :", fact)

#QO. 18 find factorial of a number(recursive).

# def factiorial(n):
#     if n == 0:
#         return 1
#     else :
#         return n * factiorial(n - 1)
    
# print(factiorial(5))

#QO. 19 find factorial of a number(recursive).

# def factorial(n):

#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))

#QO. 20 find factorial of a number(recursive).

# def factorial(n):

#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# print(factorial(5))

#QO. 21 Generate Fibonacci series up to N terms.

# n = int (input("enter number of terms:"))

# a = 0 
# b = 1

# for i in range(n):
#     print(a , end= "")

#     a, b = b, a + b

#QO. 22 Generate Fibonacci series up to N terms.

# n = int(input("enter number of terms :"))

# a = 0 
# b = 1

# for i in range(n):
#     print(a , end = "")

#     a, b = b, a + b

#QO. 23 Find largest element in a list.

# num = [2, 5, 6, 8, 67, 94, 88, 98, 34]

# print(max(num))

#QO. 24 Find smallest element in a list.

# num = [2, 5, 6, 8, 67, 94, 88, 98, 34]

# print(min(num))

#QO. 25 append any no. in a list 

# num = [2, 5, 6, 8, 67, 94, 88, 98, 34]

# num.append(23)
# print(num)

#QO. 26 Find largest element in a list.

# num = [2, 5, 6, 8, 67, 94, 88, 98, 34]

# largest = num[0] 

# for i in num :
#     if i > largest:
#         largest = i

# print("largest element is:", largest)

#QO. 27 Find smallest element in a list.

# num = [2, 5, 6, 8, 67, 94, 88, 98, 34]

# smallest = num[0]

# for i in num:
#     if i < smallest:
#         smallest = i

# print("smallest element is :", smallest)        

#QO. 28 find second largest element in a list .

# num = [10, 20, 4, 48, 94, 88]

# num.sort()
# print(num[-2])

#QO. 29 find second largest element in a list .

# num = [10, 20, 4, 48, 94, 88]

# new_list = sorted(num)
# print(new_list[-2])

#QO. 30 find second largest element in a list .

# num = [10, 20, 4, 48, 94, 88]

# largest = second = float("-inf")
# for i in num:
#     if i > largest:
#         second = largest 
#         largest = i

#     elif i > second and i != largest:
#         second = i

#         print("second largest :", second)    

#QO. 31 Find second smallest element in a list.  

# num = [10, 20, 4, 48, 94, 88]

# num.sort()
# print(num[-5])

#QO. 32 Find second smallest element in a list. 

# num = [10, 20, 4, 48, 94, 88]

# new_list = sorted(num)
# print(new_list[-5])

#QO. 33 Find second smallest element in a list. 

# num = [10, 20, 4, 48, 94, 88]

# smallest = second = float ("inf")
# for i in num:
#     if i < smallest:
#         second = smallest
#         smallest = i

#     elif i < second and i != smallest:
#         second = i

# print("second smallest :", second)        

#QO. 34 Remove duplicates from a list.

# list = [2, 10, 4, 24, 92, 88, 10]

# list.remove(10)
# print(list)

#QO. 35 Remove duplicates from a list.

# num = [2, 10, 4, 24, 92, 88, 10]

# num = list(set(num))
# print(num)

#QO. 36 Remove duplicates from a list.

# num = [2, 10, 4, 24, 92, 88, 10]

# new_list = []
# for i in num:
#     if i not in new_list:
#         new_list.append(i)

#         print(new_list)

#QO. 37 Count frequency of elements in a list.

# num = [1,2, 2, 3, 4, 1, 2]

# for i in num:
#     print(i, ":", num.count(i))

#QO. 38 Count frequency of elements in a list.

# num = [1,2, 2, 3, 4, 1, 2]

# for i in set(num):
#     print(i, ":", num.count(i))

#QO. 39 Count frequency of elements in a list.

# num = [1,2, 2, 3, 4, 1, 2]

# freq = {}
# for i in num:
#     if i in freq:
#         freq[i] += 1

#     else:
#         freq[i] = 1
# print(freq)

#QO. 40 find duplicate element in a list.

# list = [2, 3, 4, 7, 45, 67, 3, 4, 7]

# duplicate = []
# for i in list:
#     if list.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)
#         print(duplicate)

#QO. 41 find duplicate element in a list.

# num = [2, 3, 4, 7, 45, 67, 3, 4, 7]

# seen = set()
# duplicate = set()
# for i in num:
#     if i in seen :
#         duplicate.add(i)

#     else:
#         seen.add(i)
# print(list(duplicate))

#QO. 42 check if two string are anagram.

# s1 = "listen"
# s2 = "silent"

# if sorted (s1) == sorted (s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#QO. 43 check if two string are anagram.

# s1 = "listen"
# s2 = "silent"

# if sorted (s1) == sorted(s2):
#     print("Anagram")

# else:
#     print("Not Anagram")

#QO. 44 count vowels and cosonants in a strings .

# s = input("enter a string :")

# vowels = 0
# consonants = 0

# for ch in s :
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
# print("vowels:", vowels)
# print("consonants:", consonants)

#QO. 45 count vowels and cosonants in a strings .

# s = input("enter a string :")

# vowels = 0
# consonants = 0

# for ch in s :
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1

#         else:
#             consonants += 1
# print("vowels:", vowels)
# print("consonants :", consonants)           

#QO. 46 Find first non-repeating character in a string.

# s = "programing"

# for ch in s :
#     if s.count(ch) == 1:

#      print("first nun-repeating character is :", ch)
#      break

#QO. 47 find first non-repeating charater in a string.

# s = "sachin raj"

# for ch in s :
#    if s.count(ch) == 1:
      
#       print("first non- reoeating is :", ch)
#       break

#QO. 48 Find missing number in an array (1..N).

# arr = [1, 2, 4, 5]

# n=5
# for i in range(1, n+1):
#     if i not in arr :
#         print("missing number is:", i)

#QO. 49 Find missing number in an array (1..N).

# arr = [1, 2, 4, 5]
# n = 5

# for i in range(1, n + 1):
#     if i not in arr:
#         print("missing number is:", i)

#QO. 50 Find sum of digits of a number.

# num = 25

# total = 0
# for i in str(num):
#     total += int(i)

# print(total)

#QO. 51 Find sum of digits of a number.

num = 44

total = 0
for i in str(num):
    total += int(i)

print(total)

