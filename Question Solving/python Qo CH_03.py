      # CH -O3 (Topic- list in Python, list slicing, list method, tuples in puthon, touple methods)

#QO.01 WAP to ask the user to enter names of their 3 favorite movies & store them in a list.

# user = []
# user1 = input("enter first movies name: ")
# user2 = input("enter second movies name: ")
# user3 = input("enter third movies name: ")

# user.append(user1)
# user.append(user2)
# user.append(user3)

# print(user)

#QO.02 WAP to check of a list contains a palindrome of elements. (Hint: use copy() method )

# list1 = [1, 2 , 3, 2, 1]
# list2 = [1, "abc", 3, "abc", 1]

# copy_list1 = list1.copy()
# copy_list2 = list2.copy()

# copy_list1.reverse()
# copy_list2.reverse()

# if list1 == copy_list1:
#     print("list1 is palindrome")
# else:
#     print("list1 is not palindrome")

# if list2 == copy_list2:
#     print("list2 is palindrome")
# else:
#     print("list2 is not palindrome")

#QO. 03 WAP to count the number of student with the "A" grade in following tuple.

# tup = ("C", "D", "A", "A", "B", "B", "A")    

# print(tup.count("A"))


#QO. 04 WAP the above values in a list & sort them from "A" to "D".

# list = ["C", "D", "A", "A", "B", "B", "A"]

# list.sort()
# print(list)

#QO. 05 Write a program to create a list of numbers and print it.

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(list)

#QO. 06 Write a program to take a list from the user and print all elements using a loop.

# list = []
# n = int(input("enter number of elements :"))

# for i in range(n):
#     item = input("enter element: ")
#     list.append(item)

# print("elements of the list are: ")
# for item in list:
#     print(item)

#QO. 07 Write a program to find the length of a list without using the len() function.

# list = [20, 30, 40, 50, 60]

# count = 0 
# for char in list :
#     count += 1
# print("length of list is: ", count)

#QO. 08 Write a program to access the first, last, and middle element of a list using indexing.

# list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print ("first element: ", list[0])
# print ("last element: ", list[-1])
# print ("middle element :", list[len(list)//2])

#QO. 09 Write a program to perform list slicing and print:

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("first three elements:", list[ :3])
# print("last three elements:", list[ -3:])
# print(" index 2 to 5 elements:", list[ 2:6])

#QO. 10 Write a program to add an element to a list using the append() method.

# user = [55, 44, 33, 22]

# user.append(11)
# print(user)

#QO. 11 Write a program to remove an element from a list using the remove() method.

# list = [22, 44, 12, 26, 22, 44, 56]

# list.remove(22)
# print(list)

#QO. 12 Write a program to sort a list in ascending and descending order.

# list = [3, 8, 9, 4, 6, 2, 5, 1]

# list.sort()
# print("sorted list in ascending order: ", list)

# list.sort(reverse=True)
# print("sorted list in descending order: ", list)

#QO. 13 Write a program to find the maximum and minimum elements in a list.

# num = [21, 9, 29, 45, 50]

# max_val = num[0]
# min_val = num[0]

# for i in num:
#     if i > max_val:
#         max_val = i
#     if i < min_val:
#         min_val = i

# print("maximum value in list is: ", max_val)
# print("minimum value in list is: ", min_val)

#QO. 14 Write a program to count how many times a given element appears in a list.

# num = (3, 4, 8, 9, 4, 4, 10, )

# element = 4
# count = 0

# for i in num:
#     if i == element:
#         count += 1
    
# print("count of", element, "in tuple is: ", count)

#QO. 15 Write a program to create a tuple and print all its elements.

# tup = (22, 24, 26, 28, 30)

# for item in tup:
#     print(item)

#QO. 16 Write a program to access tuple elements using positive and negative indexing.

# tuo = (10, 20, 30, 40, 50)

# print("positive indexing:")
# print("element at index 0:", tuo[0])
# print("element at index 2:", tuo[2])
# print("element at index 4:", tuo[4])

# print("\nnegative indexing:")
# print("element at index -1:", tuo[-1])
# print("element at index -3:", tuo[-3])
# print("element at index -5:", tuo[-5])

#QO. 17 Write a program to find the length of a tuple and count the occurrence of an element.

# method 1: using len() and count() function
# tup = (10, 20, 30, 40 , 50, 60, 70, 80 )
# print("length of tuple is: ", len(tup))

# print("count of elements in tuple is: ", tup.count(10))  # Count occurrences of 10 in the tuple

# method 2 using loop

# tup = (10, 20, 30, 40 , 50, 60, 70, 80 )

# length = 0

# for i in tup:
#     length += 1 
# print("length of tuple is: ", length)

# tup = (10, 20, 60, 10 , 50, 60, 60, 80 )

# element = 10
# count = 0
# for i in tup:
#     if i == element:
#         count += 1

# print("count of", element, "in tuple is: ", count)
