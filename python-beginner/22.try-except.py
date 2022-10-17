# try and except block allows our program to try out a piece of code

# this helps protect our program

# try:
#     value = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except: # catches what the user did wrong 
#     print('Invalid Input')

# we can except specific types of errors

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: # catches what the user did wrong 
    print(err)
except ValueError:
    print('Invalid Input')

# we want to except a specific error instead of being too broad