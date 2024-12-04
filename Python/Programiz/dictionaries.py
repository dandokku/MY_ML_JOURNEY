#? Dictionary is a collection of key value pairs, 
person1 = {
    "name": "Dandokku",
    "age": 18
}
# name and age are the keys while Dandokku and 18 are their respective values. 
print(person1)

"""
THINGS TO NOTE
- Keys for dictionaries can be any immutable objects like tuple, numbers strings, etc. but it shouldn't be modifiable
- And each keys must be unique for identification
""" 

# Accessing Items in a dictionary. We use keys as indices for accessing items.
print(person1["name"])
# print(get["gender"]) # this helps to know if an item exists in a list or not

# Changing and adding items
person1["name"] = "Kami"
print(person1)

person1["hobbies"] = ["reading", "gaming"] #! if you  try to change items that aren't in the list, it will automatically add em as new keys and values
print(person1)

# Removing items from the dictionary
# person1.pop("name") 
print(person1.pop("name")) # this also returns the value 
print(person1)

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")


# Iterating through a dictionary
for key in person1:
    print(key) #this prints only the key
    print(person1[key]) #this prints both keys and values