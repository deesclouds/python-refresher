#  Return Statement

# create a function that cubes a number

from unittest import result


def cube(num):
    return num*num*num

print(cube(4))

# allows us to return a value back to whatever is calling the function

def cube(num):
    return num*num*num # breaks out of the function 

result = cube(4)
print(result)