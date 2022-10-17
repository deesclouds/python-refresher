# Function

# a collection of code that carries out a task
# helps organize our code and breaks them up into chunks of code


# create a function that says hi to a user

# def = keyword to say that we are creating a function
# then we name our function
# name functions with underscore
# add parenthesis after the function name 
# end it with parentheses
# then indent the next lines of code within the function
# then call our function which executes the code within our function


# def say_hi():
#     print("Hello User")


# print('Top')
# say_hi()    
# print('Bottom')

# writing function in the pythonic way
# name functions in all lowercase
# if two or more words we want to use an underscore



# parameters : a piece of information that we are giving to the function

# this function takes in two parameters
def say_hi(name, age):
    print("Hello " + name + ', you are ' + str(age))

say_hi('Dee' , 32)    
say_hi('Deesclouds', 31)    

# good to break up your code into different functions.
# if you have bits of code thats designed to execute specific tasks, thats usually a good candidate to be placed inside a function.
  