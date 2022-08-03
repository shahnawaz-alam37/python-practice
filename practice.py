# a = 4
# b = 3
# print("using the \'format\' keyword")
# print("{} + {} = {}".format(a, b,a+b))
# print("{} - {} = {}".format(a, b,a-b))
# print("{} x {} = {}".format(a, b,a*b))
# print("{} / {} = {:.2f}".format(a, b,a/b))
# print("\nusing the \'f\' keyword")
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} x {b} = {a*b}")
# print(f"{a} / {b} = {a/b:.2f}")

# name = "shahnawaz"
# print(name[0::3])
# list = [5,2,5,6,2]
# max = list[0]
# for x in list:
#     if x > max:
#         max = x

# print(max)

# inpu = input(">")

# json = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine"
# }
# output = ""
# for x in inpu:
#     output += json.get(x) + " "
# print(output)

#-------------------------- patterns -----------------------------
# for x in range(5,0,-1):       pattern = 12345     
#     for y in range(1,x+1):              1234
#         print(y,end="")                 123
#     print("")                           12
#                                         1

# for x in range(5,0,-1):       pattern = 55555
#     for y in range(-1,x-1):             4444
#         print(x,end="")                 333 
#     print("")                           22
#                                         1

# message = input(">")
# words = message.split(" ")
# emoji = {
#     ";)":"same",
#     ":)":'something else'
# }
# final_word = ''
#-----------------function----------------
# def final_word(word):
#     print(word)
# name = "shahnawaz"
# final_word(name)

# class operation:
#     def greeter(self):
#         print("Greeting...")
#     name = "shahnawaz"
# obj = operation()
# obj.greeter()
# # print(obj.name)
# Employee={"Name":"John","Age":29,"Salary":25000,"Company":"GOOGLE","Name":"John"}    
# for x,y in Employee.items():    
#     print(f"{x}:{y}")
#"""                exception handling                """

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))    
#     c = a/b
#     print(c)
    
# except ZeroDivisionError:
#     print("Invalid division")
# except ValueError:
#     print("Invalid value")

# #---------------------class methods------------------------
# class Employee:
#     def __init__(self,name):
#         self.name = name
#     def greeter(self):
#         print(f"hello! {self.name}")

# class Work(Employee):                   #single inheritance
#     def __init__(self,hrs_spent):
#         self.hrs_spent = hrs_spent
#     def print_hrs_spent(self):
#         print(f"{name} has spent {self.hrs_spent} hours at the work")

# name = input("Name:")
# emp_obj = Employee(name)
# hrs_workded = input("HRS Workded:")
# work_obj = Work(hrs_workded)
# work_obj.print_hrs_spent()


#------------------generating random numbers-----------------------------

import random
li = ['a', 'b', 'c', 'd', 'e',]
leader = (random.choice(li))
print(leader)