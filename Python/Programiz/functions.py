# A function is a group of related statements that carries out a task.
'''
def functionname():
    funtion body
'''

def greet():
    print("Hello")
    print("How you doing?")
    
greet()

# Using Arguements
def greet2(name):
    print("Hello", name)
    print("How you doing?")
    
greet2("Jack")

#! using return terminates the program wherever the return statement is called
def greet3(name):
    print("Hello", name)
    return
    print("How are you doing today?") # this won't be printed, cuz the function already terminated at  the return statement
    
greet3("Jack")

# adding multiple arguements
def add_numbers(n1, n2):
    result = n1 + n2
    return result #the return is kinda like print too

num1 = 2
num2 = 8
add_numbers(num1, num2)




print(" ")
print(" ")
print(" ")
print(" ")

#! Difference between using print and return in a function
def function_that_prints():
    print("I printed")

def function_that_returns():
    return "I returned"

f1 = function_that_prints()
f2 = function_that_returns()
print("Now let us see what the values of f1 and f2 are")
print(f1)
print(f2)

print(" ")
print(" ")
print(" ")
print(" ")


'''
Exercise1: Suppose you just attended a University examination. The marks you obtained in various subjects are stored in a list like this: marks = [55, 64, 75, 80, 65]

You want to find the average marks you obtained in the exam. And, based on the average marks you want to find your grade. The grading rule is like this:
 -You will get Grade A if the average marks is equal to or above 80
- You will get Grade B if the average marks is equal to or above 60 and less than 80
- You will get Grade C if the average marks is equal to or above 50 and less than 60
- And if the average marks is less than 50, you will get Grade F
'''
# function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks/total_subjects
    return average_marks

def find_grade(mark):
    grade = ""
    if mark >= 80:
        grade = "A"
    elif mark >= 60 and mark < 80:
        grade = "B"
    elif mark >= 50 and mark < 60:
        grade = "C"
    elif mark < 40:
        grade = "F"
    return grade

marks = [57, 90, 83, 98, 74]
average_mark = find_average_marks(marks)
grade = find_grade(average_mark)
print("Your Average mark is: ", average_mark) 
print("And your grade is: ", grade)


'''
Exericise 2: Create a program to add and multiply two numbers? For this, create two functions add_numbers() and multiply_numbers(). These functions should compute the result and return them to the function call. And, the results should be printed from outside the function.
'''
# function to add numbers
def add_numbers(n1, n2):
    result = n1 + n2
    return result

# function to multiply numbers
def multiply_numbers(n1, n2):
    result = n1 * n2
    return result

print(add_numbers(2, 5))
print(multiply_numbers(5, 6))
