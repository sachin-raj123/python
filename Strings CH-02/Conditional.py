               # Conditional Statements

          # if statement

# age = 23

# if(age >= 18):
#     print("you can vote")
#     print("you can drive")

         # elif statement
 
# light = "green"

# if(light == "red"):
#     print("stop")

# elif(light == "green"):
#     print("go")

# elif(light == "yellow"):
#     print("wait")

# print("end of code ")

            # else statement

# age = 34 

# if(age >= 18):
#     print("you can vote")
# else:
#     print("you can not vote")    


marks = int(input("enter stuedent marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"    
else:
    grade = "D"  

print("grade of the student ->", grade)

 