                                            
                                             # PYTHON TEST ALL QUESTIONS

#QO. 01 check Armstrong number . 

# num = int(input("enter a number:"))

# temp = num
# digits = len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10 
#     sum += digit ** digits
#     temp = temp // 10

#     if sum == num:
#         print("Armstrong number")
#     else:
#         print("Not Armstrong number")

#QO. 02  check Armstrong number

# num = int(input("enter a number:"))

# temp = num 
# digits = len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits
#     temp = temp // 10

#     if sum == num:
#         print("Armstrong number")
#     else:
#         print("Not Armstrong number")

#QO. 03  Check perfect number.

# num = int(input("enter a number:"))
# sum = 0

# for i in range(1 , num):
#     if num % i == 0:
#         sum += i

#         if sum == num:
#             print("perfect number")
#         else:
#             print("Not perfect number")

#QO. 04 check perfect number.

# num = int(input("enter a number:"))
# sum = 0

# for i in range(1 , num):
#     if num % i == 0:
#         sum += i

#         if sum == num:
#             print("perfect number")
#         else :
#             print("Not perfect number")

#QO. 05 check leap year .

# year = int(input("enter a year :"))

# if (year % 4 == 0 and year % 100 != 0):
#     print("leap year")

# else:
#     print("not leap year")

#QO. 06 check leap year

# year = int(input("enter a year:"))

# if (year % 4 == 0 and year % 100 != 0):
#     print("leap year")

# else:
#     print("not a leap year")

#QO. 07 Swap two numbers without temp variable.

# val1 = int(input("enter a value :"))
# val2 = int(input("enter a value :"))

# val1, val2 = val2 , val1

# print("after swapping :")
# print("first number :", val1)
# print("second number:", val2)

#QO. 08 Swap two numbers without temp variable.

# num1 = int(input("enter a nums :"))
# num2 = int(input("enter a nums :"))

# num1, num2 = num2, num1

# print("after swaping:")
# print("first number:", num1)
# print("second number:", num2)

#QO. 09 Print star pattern (triangle/pyramid).

# n = int(input("enter number of rows:"))

# for i in range(1, n+1):
#     print("*" * i)

#QO. 10 Print star pattern (triangle/pyramid).

# n = int(input("enter number of rows :"))

# for i in range(1, 1+n):
#     print(" " *(n-i), end = "")
#     print("*" *(2*i-1), end = "")
#     print("")

#QO. 11 Sort a list without using sort().

# lst = [5, 4, 8, 9, 1, 3, 2, 6]

# n = len(lst)

# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]

# print("Sorted list:", lst)

#QO. 12 Sort a list without using sort().

# lst = [4, 3, 8, 9, 1, 3, 2, 6]

# n = len(lst)

# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]

# print("Sorted list:", lst)

#QO. 13 Sort a list without using sort().

# lst = [7, 1, 5, 9, 2, 7, 4, 8]

# n = len(lst)

# for i in range(n):
#     for j in range(i + 1, n):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]

# print("Sorted list:", lst)

#QO. 14 Bubble sort implementation.

# list = [4, 8, 9, 7, 6, 2, 3, 5]

# n = len(list)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if list[j] > list[j + 1]:
#             list[j], list[j + 1] = list[j + 1], list[j]

# print("sorted list :", list)

#QO. 15 Bubble sort implementation.

# num = [4, 8, 9, 2, 6, 1, 3, 5, 7]

# n = len(num)
# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if num[j] > num[j + 1]:
#             num[j], num[j + 1] = num[j + 1], num[j]

# print("sorted list :", num)

#QO. 16  Selection sort implementation.

# vals = [2, 4, 6, 8, 10, 3, 1, 5, 7, 9]

# n = len(vals)
# for i in range(n - 1):
#     min_index = i

#     for j in range(i + i, n):
#         if vals[j] < vals[min_index]:
#             min_index = j

#             vals[i], vals[min_index] = vals[min_index], vals[i]
# print("sorted list:", vals)            

#QO. 17  Selection sort implementation.

# num = [2, 4, 6, 8, 10, 3, 1, 5, 7, 9]

# n = len(num)
# for i in range(n - 1):
#     min_index = i

#     for j in range(i + i, n):
#         if num[j] < num[min_index]:
#             min_index = j

#             num[i], num[min_index] = num[min_index], num[i]
# print("sorted list:", num) 

#QO. 18 Insertion sort implementation.

# num = [5, 4, 8, 9, 1, 3, 2, 6]

# n = len(num)
# for i in range(1 , n):
#     key = num[i]
#     j = i - 1

#     while j >= 0 and num[j] > key :
#         num[j + 1] = num [j]
#         j -= 1

#         num[j + 1] = key
# print("sorted list :", num)

#QO. 19 Insertion sort implementation.

# a = [5, 4, 8, 9, 1, 3, 2, 6]

# n = len(a)
# for i in range(1 , n):
#     key = a[i]
#     j = i - 1

#     while j >= 0 and a[j] > key :
#         a[j + 1] = a [j]
#         j -= 1

#         a[j + 1] = key
# print("sorted list :", a)

#QO. 20 Binary search implementation.

# num = [5, 2, 8, 7, 9, 6]
# target = int(input("enter a number:"))

# low = 0
# high = len(num) - 1
# found = False

# while low <= high:
#     mid = (low + high) // 2

#     if num[mid] == target :
#         print("element found at index :", mid)
#         found = True
#         break

#     elif num[mid] < target:
#         low = mid + 1

#     else:
#         high = mid -1

#         if not found:
#          print("element not found :")

#QO. 21 Linear search implementation.

# num = [10, 25, 40, 35, 60]

# key = 40
# if key in num:
#     print("element found")
# else:
#     print("element not found")

#QO. 22 Linear search implementation.

# list = [10, 25, 40, 35, 60, 50 , 45]

# key = int(input("enter a number :"))
# found = False

# for i in range(len(list)):
#     if list [i] == key:
#         print("element found :", i)
#         found = True
#         break

#     if not found:
#      print("element not found")

#QO. 23 Linear search implementation.

# value = [10, 25, 40, 35, 60, 50 , 45]

# key = int(input("enter a value :"))
# found = False

# for i in range(len(value)):
#     if value [i] == key:
#         print("element found :", i)
#         found = True
#         break

#     if not found:
#       print("element not found")

#QO. 24 Find GCD of two numbers.

# a = int(input("enter a number :"))
# b = int(input("enter a number :"))

# gcd = 1
# for i in range(1, min(a, b) + 1):
#    if a % i == 0 and b % i == 0:
#       gcd = i

# print("GCD is :", gcd)

#QO. 25 Find GCD of two numbers.

# num1 = int(input("enter a number :"))
# num2 = int(input("enter a number :"))

# gcd = 1
# for i in range(1, min(num1, num2) + 1):
#    if num1 % i == 0 and num2 % i == 0:
#       gcd = i

# print("GCD is :", gcd)

#QO. 26  Find LCM of two numbers.

# a = int(input("enter a number :"))
# b = int(input("enter a number :"))

# max_num = max (a , b)
# while True :
#     if max_num % a == 0 and max_num % b == 0:
#         print("LCM is :", max_num)

#         break
#     max_num += 1

#QO. 27  Find LCM of two numbers.

# values1 = int(input("enter a number :"))
# values2 = int(input("enter a number :"))

# max_num = max (values1 , values2)
# while True :
#     if max_num % values1 == 0 and max_num % values2 == 0:
#         print("LCM is :", max_num)

#         break
#     max_num += 1

#QO. 28 Reverse a list.

# list = [3, 6, 8, 1, 5, 9, 2, 4]

# list.reverse()
# print(list)

#QO. 29 Reverse a list.

# num = [3, 6, 8, 1, 5, 9, 2, 4]

# rev = num[:: -1]
# print(rev)

#QO. 30 Reverse a list.

# call = [3, 4, 5, 8, 2, 6, 1]

# rev = []

# for i in range(len(call)-1, -1, -1):
#     rev.append(call[i])

# print(rev)

#QO. 31 Rotate a list by K positions.

# num = [1, 2, 3, 4, 5] 
# k = 1

# rotated = num[k:] + num[: k]
# print(rotated)

#QO. 32 Rotate a list by K positions.

# numbers = [1, 2, 3, 4, 5] 
# k = 2

# for i in range(k):
#     first = numbers.pop(0)
#     numbers.append(first)

# print(numbers)

#QO. 33  Merge two sorted lists.

# num1 = [1, 2, 4, 6, 8]
# num2 = [3, 5, 7, 9]

# merged = num1 + num2
# merged.sort()
# print(merged)

#QO. 34  Merge two sorted lists.

# val1 = [1, 2, 4, 6, 8]
# val2 = [3, 5, 7, 9]

# merged = val1 + val2
# merged.sort()
# print(merged)

#QO. 35 Find intersection of two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7, 8]

# intersection = list(set(list1) & set(list2))
# print("common value of :", intersection)

#QO. 36 Find intersection of two lists.

# sub1 = [1, 2, 3, 4, 5]
# sub2 = [3, 4, 9, 6, 7, 8]

# intersection = list(set(sub1) & set(sub2))
# print("common value of :", intersection)

#QO. 37 Find union of two lists.

# sub1 = [1, 2, 3, 4, 5]
# sub2 = [3, 4, 9, 6, 7, 8]

# union = list(set(sub1) | set(sub2))

# print("combines both set val :", union)

#QO. 38 Find union of two lists.

# num1 = [1, 2, 3, 4, 5]
# num2 = [3, 4, 9, 6, 7, 8]

# union = num1.copy()
# for item in num2:
#     if item not in union:
#         union.append(item)

# print(union)

#QO. 39 Find union of two lists.

# val1 = [2, 3, 4, 5, 6]
# val2 = [1, 7, 8, 9, 2, 5]

# union = val1.copy()
# for item in val2:
#     if item not in union:
#         union.append(item)

# print("the union of :", union)

#QO. 40 Find common elements between two lists.

# num1 = [10, 12, 14, 16, 18]
# num2 = [16, 18, 20, 22, 24, 26]

# common = list(set(num1) & set(num2))

# print("common element :", common)

#QO. 41 Find common elements between two lists.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8, 9]

# common = []
# for item in list1:
#     if item in list2:
#         common.append(item)

# print("common element :", common)

#QO. 42 Check if list is sorted.

# list = [2, 4, 6, 8, 9, 5, 3, 1, 6, 7]

# if list == sorted(list):
#     print("list is sort")
# else:
#     print("list is not sort")

#Q0. 43 Check if list is sorted.

# elem = [2, 4, 6, 8, 9, 5, 3, 1, 6, 7]

# if elem == sorted(elem):
#     print("list is sort")
# else:
#     print("list is not sort")

#QO. 44 Implement stack using list.

# stack = []

# stack.append(12)
# stack.append(14)
# stack.append(16)

# print("stack after push:", stack)
# stack.pop()
# print("stack after pop:", stack)

#QO. 45 Implement stack using list.

# num = []
# num.append(10)
# num.append(20)
# num.append(30)


# print("stack after push :", num)
# num.pop()
# print("stack after pop :", num)

#QO. 46  Implement queue using list / collections.deque.

# queue = []
# queue.append(6)
# queue.append(8)
# queue.append(10)

# print("Queue after push :", queue)
# queue.pop(0)
# print("Queue after pop:", queue)

#QO. 47  Implement queue using list / collections.deque.

# input = []
# input.append(60)
# input.append(80)
# input.append(100)

# print("Queue after push :", input)
# input.pop(0)
# print("Queue after pop:", input)

#QO. 48  Count words in a sentence.

# sachin = "i am sachin raj"

# count = 1
# for ch in sachin:
#     if ch == "":
#         count += 1

# print("number of words :", count)

#QO. 49  Count words in a sentence.

# val = " hi i am sachin raj"

# words = val.split()
# count = len(words)

# print("Number of words:", count)

#QO. 50 Find longest word in a sentence.

# sentance = " i am learning python programing "

# longest = max (sentance.split(), key = len)
# print("longest word is :", longest)

#QO. 51 Find longest word in a sentence.

# word = " i am learning python programing "

# longest = max (word.split(), key = len)
# print("longest word is :", longest)

#QO. 52 Replace spaces with hyphen in a string.

# word = "i am learning python programing"

# print(word.replace(" ","-"))

#QO. 53 Replace spaces with hyphen in a string.

# word = "i am learning python programing"
# word = word.strip()
# print(word.replace(" ","-"))

#QO. 54 Count occurrence of a character in a string.

# str = "Banana"

# ch = 'a'
# print("count occurrence of:", str.count(ch))

#QO. 55 Count occurrence of a character in a string.

# word = "Banana"

# ch = 'a'
# count = 0
# for i in word:
#     if i == ch:
#         count = count + 1
# print("count occurrence of:", count)

#QO. 56 Convert string to title case without built-in.

# string = "i am sachin raj"

# result = ""
# new_word = True

# for ch in string:
#     if ch == " ":
#         result += ch
#         new_word = True
#     elif new_word:
#         result += ch.upper()
#         new_word = False
#     else:
#         result += ch.lower()

# print(result)

#QO. 57 Convert string to title case without built-in.

# sentense = "i am sachin raj"

# result = ""
# new_word = True

# for ch in sentense:
#     if ch == " ":
#         result += ch
#         new_word = True
#     elif new_word:
#         result += ch.upper()
#         new_word = False
#     else:
#         result += ch.lower()

# print(result)

#QO. 58 Find all substrings of a string.

# string = input("enter a string :")

# n = len(string)
# for i in range(n):
#     for j in range(i + 1 , n + 1):
#      print(string[i : j])

#QO. 59 Find all substrings of a string.

# value = input("enter a string :")

# n = len(value)
# for i in range(n):
#     for j in range(i + 1 , n + 1):
#      print(value[i : j])

#QO. 60 Check if number is palindrome.

# num =[1, 2, 3, 2, 1]

# if num == num[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#QO. 61 Check if number is palindrome.

# sub =[5, 6, 7, 6, 5]

# if sub == sub[::-1]:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")

#QO. 62 Print multiplication table of a number.

num = int(input("enter a number :"))

for i in range(1 , 11):
    print(num , "x" , i , "=", num * i)

#QO. 63 Print multiplication table of a number.

sub = int(input("enter a number :"))

for i in range(1 , 11):
    print(sub , "x" , i , "=", sub * i)


