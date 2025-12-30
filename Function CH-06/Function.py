               # Function definition


# def calc_sum(a, b):       # parameters: a, b
#     """Calculate the sum of two numbers."""
#     return a + b

# sum = calc_sum(5, 10)  # arguments: 5, 10  and # function call
# print(sum)  # Output: 15

# def print_hello():
#     """Print a hello message."""
#     print("Hello, World!")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# output = print_hello()
# print(output)    #None

          # average of 3 numbers

# def calc_avg(a,b, c):
    
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(83, 98, 79)

            # Default Parameter Values

# def cal_prod(a, b=2):
#     print(a * b)
#     return a * b

# cal_prod(10)

 
                # Recursive Function 


# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)                

# show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))
     
  