             # practice QO NO. 01

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:", sum/3)

# s1 = student("tiny stark", [99, 98, 97])
# s1.get_avg()    
         

             # practice QO NO. 02

# class account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited") 
#         print("total balance = ", self.get_balance())
        
#     def credit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was credited") 
#         print("total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.balance
    
# acc1 = account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)


                # practice QO NO. 03

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2 

    def perimeter(self):
        return 2 * (22/7) * self.radius


c1 = circle(21)
print(c1.area())
print(c1.perimeter())
