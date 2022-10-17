# for loop - loop through array, strings, series of numbers

# used for a specific purpose

for letter in "deesclouds":
    print(letter)

# letter variable prints out each letter from the string deesclouds

friends = ['Jim', 'Karen', 'Kevin']
for friend in friends:
    print(friend)

# friend is our iterable which can be named whatever we want. 

friends = ['Jim', 'Karen', 'Kevin']
for index in range(10):
    print(index)

#prints out all the numbers between 0 and 10 without printing 10

for index in range(3, 10):
    print(index)

# prints out all the numbers between 3 and 10 without printing 10.
# whatever number we stop at will not be printed.

# get the length of the array
friends = ['Jim', 'Karen', 'Kevin']
for index in range(len(friends)):
    print(friends[index])

# prints out the strings within the array of friends

friends = ['Jim', 'Karen', 'Kevin']
for index in range(len(friends)):
    print(index)
# prints out the indexes of the friends array

friends = ['Jim', 'Karen', 'Kevin']
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")