'''
- Difference between return and print: print just displays on the screen for the human user, it does not really have any computational value. But return stores the value, usually a function is supposed to return a value, if you use print--it'll return null as the value. when working with functions, return is a better statement to use.



- Keyword Argument: 
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



- Avoiding the global keyword, what should i use instead: It is better to pass the variable as an argument to the function and return the modified value. e.g:

age = 30

def greeting(age):
    age = age + 5
    return age


- the self parameter in classes/methods


'''