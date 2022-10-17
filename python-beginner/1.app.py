# BASIC PROGRAM
from curses.ascii import isupper
from math import *  #imports more math functions that we can use


print('Hello')

# DRAWING SHAPES
print('    /|')
print('   / |')
print('  /  |')
print(' /   |')
print('/____|')

# shows that python runs our script in order from top to bottom

# VARIABLES AND DATA TYPES

character_name = 'George' #string
is_male = False #boolean
character_age = '35' #int


print('There once was a man named ' + character_name + ',')
print('he was ' + character_age + ' years old. ')

# updated the variable within the program
character_name = 'Mike'
print('He really liked the name ' + character_name + ', ')
print('but didn\'t like being ' + character_age + '.')

# STRINGS
print("Deesclouds\nTutorial")
#create a string variable
phrase = 'deesclouds'
print(phrase + ' is dope af')

# FUNCTIONS
print(phrase.lower()) # converts variable to lowercase
print(phrase.upper()) #converts variable to uppercase
print(phrase.isupper()) #checks if variable is uppercase
print(phrase.upper().isupper()) #converts variable to uppercase then checks if its uppercase
print(len(phrase)) # checks the length of characters
print(phrase[0]) #checks the first index within the string variable
print(phrase.index("deesclouds")) #returns the index within the string 
print(phrase.replace('clouds','dope')) # replace certain words or letters within a string

# NUMBERS
print(3 + 4.5) # addition
print(3 * (4 + 5)) # pemdas
print(10 % 3) # modulus = remainder

# STORING NUMBERS within VARIABLES
my_num = 5
print(my_num)

my_num = 5
print(str(my_num) + ' is my favorite number') # make sure to use the str function

# ARITHMETIC OPERATIONS

a_num = -5
print(abs(a_num)) #absolute num

print(pow(3, 2)) # exponents

print(max(4,6)) # returns the highest number

print(min(4, 6)) # returns the lowest number

print(round(3.2)) #rounds to a whole number

print(floor(3.7)) # removes the decimal number

print(ceil(3.7)) # rounds the number up

print(sqrt(36)) #returns the square root