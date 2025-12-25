             # Set in Python  #

# collection = {1, 2, 3, 2, 2, "hello",  "world", "world", 4.5, 4.5}

# print(collection)
# print(type(collection))
# print(len(collection))


# collection = set()      # empty set
# print(type(collection))

               # Set Methods  #


  # Add Method  #   
# collection = set()
# collection.add(1)
# collection.add(2)   
# collection.add(3)
# collection.add(2)    # duplicate value will not be added

# print(collection)
# print(len(collection))

 
    # Remove Method  #
# collection = set()
# collection.add(1)
# collection.add(2)   
# collection.add(3)
# collection.add(2) 

# collection.remove(2)   # removes 2 from set
# print(collection)
# print(len(collection))

 
    # Clear Method  #
# collection = set()
# collection.add(1)
# collection.add(2)   
# collection.add(3)
# collection.add(2) 

# collection.clear()   # removes all elements from set
# print(collection)
# print(len(collection))


    # Pop Method  #
# collection = set()
# collection.add(1)
# collection.add(2)   
# collection.add(3)
# collection.add(4)    
# collection.add(5)    
# collection.add(6)    
# collection.add(7)    
# collection.add(1)    
# collection.add(0)    
# collection.add(9)    

# collection.pop()   # removes arbitrary element from set
# print(collection)
# print(len(collection))

# collection = {"apple", "banana", "cherry", "date", "fig", "grape"}

# print(collection.pop())   # removes arbitrary element from set
# print(collection.pop())   # removes arbitrary element from set


  # Union Method  #
# set1 = {1, 2, 3, 4}
# set2 = {4, 5, 6, 7}

# union_set = set1.union(set2)
# print(union_set)
# print(len(union_set))


    # Intersection Method  #
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}  

print(set1.intersection(set2))
print(len(set1.intersection(set2)))

