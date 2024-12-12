'''
Inheritance allows us to inherit attributes and methods from a parent class to child classes.
Imagine a base vehicle class with children classes like cars, motocycles, airplanes etc and they all inherit some attributes and methods like features.
This helps for code reusuability


'''

class Animal:
    def eat(self):
        print("I can Eat? wtf")

class Dog(Animal):
    def bark(self):
        print("I can bark")
        
    #! the dog class inherits all the methods from the animal class

class Cat(Animal, Dog):
    def getGrumpy(self):
        print("I dey vex like this.")

dog1 = Dog()
dog1.eat() #see?        

cat1 = Cat()
cat1.eat()
cat1.bark() 
#! DAMNN, YOU CAN INHERIT MULTIPLE CLASSES TOO