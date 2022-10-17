# parsing information within a file

# # open file within the same directory and read
# open('employees.txt', "r")

# # open file and write
# open('employees.txt', "w")

# # open and append
# open('employees.txt', "a")

# # open file, read and write
# open('employees.txt', "r+")

# # open and store within a variable
# employee_file = open('employees.txt', "r")
# print(employee_file.readable())

# # when opening a file we want to also close the file
# employee_file.close()

# # open and store within a variable and able to read the file
# employee_file = open("employees.txt", "r")
# print(employee_file.read())
# employee_file.close()

# # read an individual line
# employee_file = open("employees.txt", "r")
# print(employee_file.readline())
# employee_file.close()

# # read multiple line and place them within a list
# employee_file = open("employees.txt", "r")
# print(employee_file.readlines())
# employee_file.close()

# use a for loop to read multiple line within a file and prints each line
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()