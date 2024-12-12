# Classes and Objects

'''
A class is like a blueprint of a house, it contains all the details about the floors, doors, windows, etc. Based on these description we build the house. The house is the object, so we can creat many objects from a single class; think about having many resources in minecraft, you can build different things(obejects) from the class(resources) that you have
'''

# Class
class Student: #creating a class
    def check_pass_fail(self): #creating a method inside the class, always pass self as the first argument (self is a convention, for consistency)
        if self.marks >= 40:
            return True
        else:
            return False   
        
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
student2 = Student("Dandokku", 89)
student3 = Student("Kami", 98)
print(student2.marks) # oh
# ! manually adding  attributes to classes ain't really advisable, so it's is better to use the init method. The init method is a special method that automatically gets called everytime objects are created.
# student1 = Student() #! student1 in this case is an object of the class Student()
# student1.marks = 41

# print(student1.check_pass_fail())



# Example2: adding two complex numbers
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = Complex(real, imag)
        return result

n1 = Complex(5, 3)
n2 = Complex(4, 2)
result = n1.add(n2)
print(result.real)
print(result.imag)  


# Exercise
class Triangle: # create the class
    def __init__(self, a, b, c): # initialises the arguements
        self.a = a
        self.b = b
        self.c = c
    
    def getPerimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
        
triangle1 = Triangle(5, 5, 5)
# thePerimeter = Triangle.getPerimeter(triangle1) #! this works tho (class method format)
thePerimeter = triangle1.getPerimeter() #! but this is better, this is called using an instance method
print(thePerimeter)



#! Explaining the difference between instance method and class method
class Circle:
    pi = 3.14  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable

    def area(self):  # Instance method
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):  # Class method
        radius = diameter / 2
        return cls(radius)  # Create an instance of Circle

# Using instance method
circle1 = Circle(5)
print(circle1.area())  # Calls the instance method

# Using class method
circle2 = Circle.from_diameter(10)
print(circle2.area())  # Calls the instance method on a new instance

#! So basically the instance method is more specific. i dig i dig


# Everything in python is a object

numbes = [1, 3, 4, 5]
print(type(numbes))

n1 = 5
print(type(n1))
# as you can see, they are all objects


#? dir(), You can list out all the attributes and methods of a given object by using the dir() function
print(dir(numbes)) #crazy shit mann

# welp = numbers.__add__([3, 4, 6])
# print(welp)


#? id(), every object has an id for identity. The id of an object is always unique and constant for this object during its lifetime
print(id(numbes)) 
print(id(n1)) 
# The id differs everytime, why?
