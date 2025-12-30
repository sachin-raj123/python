                # practice QO NO.  01

# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

# heroes = ["thor", "spiderman", "ironman", "hulk", "captain america"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)


                # practice QO NO.  02

# heroes = ["thor", "spiderman", "ironman", "hulk", "captain america"]                 

# # print(heroes[0], end=" ")
# # print(heroes[1], end=" ")
# # print(heroes[2], end=" ")
# # print(heroes[3], end=" ")
# # print(heroes[4], end=" ")

# def print_len(list):
#     print(len(list))


# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print_list(heroes)

              
                 # practice QO NO.  03

# n = 5

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)

# cal_fact(5)


                  # practice QO NO.  04

# def converter (usd_val):
#     inr_val = usd_val * 90
#     print(usd_val, "USD =", inr_val, "INR")

# converter(1000)


                  # practice QO NO.  05

# write a recursive function to calculate the sum of first n natural no .
    
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)
 
