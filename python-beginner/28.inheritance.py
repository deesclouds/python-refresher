from Chef import Chef #importing the Chef class
from ChineseChef import ChineseChef

myChef = Chef() #creating a new chef
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()
myChineseChef.make_chicken()

# inheritance define attributes and functions within a class, then create another class that inherits those attributes. without having to write all those functionalities or attributes.

# inherits functionality from an existing class
