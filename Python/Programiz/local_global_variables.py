def add_numbers(n1, n2):
    result = n1 + n2
    return result

output = add_numbers(5, 3)
#print(result) #! Result in this case is a local variable, it can't be accessed outside the function, so this will return an error
print(output) #! this would work


# GLobal Variable
message = "How are yo doing?"

def greet():
    # global message #! when this is enabled, the global variable message would be changed to "How are you?"
    message = "How are you?"
    print("Inide: ", message)
    
greet()
print("Outside: ", message)

# Avoiding the global keyword, what should i use instead: It is better to pass the variable as an argument to the function and return the modified value. e.g:
age = 30

def greeting(age):
    age = age + 5
    return age


'''
SUMMARY:
- A variable defined inside a function is local to it. When the function ends, this variable is destroyed
- Variables defined outside a function are called global variables in python
- Inside functions, the global keyword can be used to change the value of a variable in the global scope
- Using the global keyword is a bad practice, and you should try to avoid it whenever possible
'''