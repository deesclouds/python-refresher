# Comparison operators 

# >= : greater than or equal to
# == : checks if two values are equal
# != : not equal
# <= : less than or equal to
# > : greater than
# < : less than



# Creating a python function that give us the biggest number within  our parameters

def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

print(max_num(300, 40, 5))

