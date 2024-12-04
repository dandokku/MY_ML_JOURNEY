# The range function  in loops is used to run a loop a certain number of times. Though it has a lot of use cases

result = range(1, 11) # this returns 1 to 10, cuz it doesn't include the last value
print(result) # won't show you shit
print(list(result)) # convert the shii into a list in order to see what is in the kini

# In for loops
for value in range(1, 6):
    print(value, "welp")
    
""" 
range() with only stop parameter: usually there are three parameters(start, stop, step), in our case; 1 is the start parameter and 6 is the top parameter. What happens when you only pass in the stop parameter: Well, when you don't pass in the start parameter, it'll automatically compute it as 0
"""
print(list(range(6)))

for value in range(5):
    print("daMN!")
    
    
"""
range() with step parameter
"""
print(list(range(1, 11))) # since we didn't add a step parameter, the default value is 1

print(list(range(1, 11, 2))) # [1, 3, 5, 7, 9]

# Range only works for integers btw

# EXercise
print(list(range(3, 31, 3)))