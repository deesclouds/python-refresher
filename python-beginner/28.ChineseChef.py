from Chef import Chef

class ChineseChef(Chef): #inherits all the functions from the Chef class
    def make_special_dish(self): # overriding the inherited function by printing a new line 
        print('The chef makes orange chicken')
    def make_fried_rice(self):
        print('The chef makes fried rice')