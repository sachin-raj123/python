            # Class & Object in Python 

# class student:
#     name = "sachin raj"    # (Class)

# s1 = student()
# print(s1.name)           
                       
# s2 = student()        #(Object)
# print(s2.name)


# class car:
#     color = "blur"
#     model = "bugatti"

# car1 = car()
# print(car1.color)
# print(car1.model)

 
               # __init__ Function

# class student: 

#          # default constructors
#     def __init__(self):
#        pass

#      # parameterized constructors
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in Database..")


# s1 = student("sachin", 87)
# print(s1.name, s1.marks)    # karan

# s2 = student("arjun", 77)
# print(s2.name, s2.marks)


               #  Oops methods

# class student:
#     collage_name = "SVIET collage"

#     def __init__(self,name,marks):
#       self.name = name
#       self.marks = marks

#     def welcome(self):
#          print("welcome student")

#     def get_marks(self):
#         return self.marks
     
# s1 = student("karan", 97)
# s1.welcome()
# print(s1.get_marks())   


             # Static method 

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod            # decorator
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:", sum/3)

# s1 = student("tiny stark", [99, 98, 97])
# s1.get_avg()
# s1.hello()   


             # Abstraction

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()            

