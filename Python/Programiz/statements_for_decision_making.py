# IF and ELSE statements
# syntax
'''
if test_condition:
    statement()

'''

# Exercise: Suppose you are a student and to pass the examination you need to score 50 or more. If your score is 50 or more, print" You have passed your exam"
score = int(input("What is your score: "))
if score >= 50:
    print("CONGRATS!! You have passed the exam!")
elif score <= 49 and score >= 25:
    print("You almost passed! ")
else: 
    print("Pele, you failed :(")    


#* Exercise 2: Create a program to check whether a number positive or negative or 0. For this, create a variable named number and assign a float value to it based on the user input. Then using a if statement, check if the number variable is positive or negative or 0.
number = float(input("Enter a number:"))
if number > 0:
    print(number, " is a positive number")
elif number < 0:
    print(number, " is a negative number")
elif number == 0:
    print(number, " is 0")
else:
    print("wtf is that?")
    
    
    