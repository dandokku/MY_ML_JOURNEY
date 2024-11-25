#  Arithmetic Operators
'''
- Addition * 
- Subtraction -
- Multiplication *
- Division /
- Exponent **
- Floor Division //
- Remainder %
'''

name = "Dandokku" # = is an assignment operator btw

# Addition
a = 1
b = 2
c = (a + b)
print(c)

# Subtraction
aa = 2
bb = 1
cc = aa - bb
print(cc)

# Multiplication
w = 5
e = 2
g = w * e
print(g)

# Exponent (raising to the power of)
print(2 ** 2)

# Division 
print(8/2)

# Floor Division
print(10//2)

# Remainder
print(10%3)



# Assignment Operators
# = or +=


# EXERCISE - what amount should you pay if the tuition fee is 4535 and you got a 10% discount
tf = 4535
discount = (tf / 100) * 10
fee = tf - discount
print("You got a 10% discount and your tuition fee is: ", fee)

# EXERCISE 2 - converting distance  in km to miles
distance = 500
miles = 0.621371
distance_in_miles = distance / miles
print(distance_in_miles)



# Comparision Operator
'''
< less than
> greater than
== equal
!= not equal
>= greater than or equal to
<= less than or equal to
'''

# less than
number = 2
print(number < 1)

# greater than
number = 15
print(number > 10) #is the number greater than 10

# equal
number = 10
print(number == 10)

# not equal
number = 102
print(number != 102)

# greater than or equal to
number = 11
print(number >= 20)

# less than or equal to
number = 10
print(number <= 10)



# Logical Operators
'''
and - True if both operands are True
or - True if either of the operands is True
not - True
''' 

# and
age = 22
gpa = 4.0 
result = age >= 18 and gpa > 4.1
print(result)

# or
age = 22
gpa = 4.0 
result = age >= 22 or gpa > 4.1
print(result)


# not
welp = False
print(not welp)
