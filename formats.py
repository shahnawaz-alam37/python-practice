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
# print(obj.name)
Employee={"Name":"John","Age":29,"Salary":25000,"Company":"GOOGLE","Name":"John"}    
for x,y in Employee.items():    
    print(f"{x}:{y}")