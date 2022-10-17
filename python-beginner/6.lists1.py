# updating lists 

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Tim']
friends.extend(lucky_numbers) # add two lists together
print(friends)

friends.append('Creed') # add another item to the end of a list 
print(friends)

friends.insert(1, "Kelly") # can update the list with an item within the index
print(friends)

friends.remove('Jim')
print(friends)

friends.clear() # clears all the elements from a list
print(friends)

friends = ['Kevin', 'Karen', 'Jim', 'Jim', 'Oscar', 'Tim']
friends.pop() # removes last element within a list
print(friends)

print(friends.index('Kevin')) # checks to see if a value is within the list

print(friends.count('Jim'))

friends.sort() # sorts friends in ascending order (alphabetic order)
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse() # places a list in descending order
print(lucky_numbers)

friends2 = friends.copy() # copies a list and places it within another variable
print(friends2)