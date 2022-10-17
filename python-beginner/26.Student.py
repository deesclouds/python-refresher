# creating our student data type
# class = is an overview that's defining what a student is 
class Student:
    # initialized function
    # model out what attributes a student should have as parameters
    def __init__(self, name, major, gpa, is_on_probation):
        # assigning some values to the object to = the parameter
        # self refers to the actual object
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


