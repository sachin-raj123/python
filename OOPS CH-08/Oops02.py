             # Del keyboard

# class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("sachin")
# print(s1.name)
# del s1.name
# print(s1.name)        
        

             # Inheritance  ( Single Inheritance)

# class car:

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, name):
#        self.name = name

# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")

# print(car1.start())


                 # Inheritance  ( Multi - Level Inheritance)
             
# class car:

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, brand):
#        self.name = brand

# class Fortuner(toyotacar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()        
        

              # Inheritance  ( Multiple  Inheritance)

# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)  


# class Car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")


# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name 
#         super().start()


# car1 = ToyotaCar("prius", "electric")
# print(car1.type)
               

                 # class method 

# class Person:
#     name = "anonymous"
       
#     #   def chnageName(obj, name):
#     #     self.__class__.name = "Rahul"

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name               


# p1 = Person()
# p1.changeName("Rahul kumar")
# print(p1.name)
# print(Person.name)


                # Property Decorators - Getters and Setters

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(98, 97, 99)
# print(stu1.percentage)

# stu1.phy = 86
# print(stu1.percentage)


                # Operator Overloading ( Dunder function )


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")


    def __add__(self, num2):
        newreal = self.real + num2.real
        newimg = self.img + num2.img
        return Complex(newreal, newimg)

num1 = Complex(1, 3)
num1.showNumber()    

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

 