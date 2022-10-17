# Dictionaries - for storing different types of data.

# lets us store values in key value pairs
#  key: value pair
# keys must be unique

monthConversions = {
    "Jan": "January", 
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# accessing our dictionary
print(monthConversions)

# accessing by key - prints value associated with that key
print(monthConversions['Nov'])

print(monthConversions.get('Dec'))

# accessing a key that is not within the dictionary returns None
print(monthConversions.get('Luv'))

# prints a default value to fall back on
print(monthConversions.get('Luv', 'Not a valid Key'))

