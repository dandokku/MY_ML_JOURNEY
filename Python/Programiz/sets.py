"""
Sets in python are similar to how set works in maths
A set is a collection of  similar items

- Items of a set are not in order
- No duplicate items are allowed
- Sets are mutable, meaning you can add or remove elements after creating them, though the individual elements within the set must be immutable and cannot be changed directly 
"""
animals = {"dog", "tiger", "cat", "donkey", "cat"}
print(animals) # there's is no particular order, also notice that the duplicate items were removed.

# To create an empty set, use the set function
animal = set()
print(animal)

# The set function can also be used to create  non empty sets
anima = set(["dog", "tiger", "cat", "donkey", "cat"]) #! in this case, the list was converted into a set, and i bet you can do that for most of the others (tuples, dictionaries and strings), right?
mylist = ["dog", "tiger", "cat", "donkey", "monkey"]
listset = set(mylist)
print(type(listset)) #! YEp, the shit works

# Updating items in a set(adding sets to sets too)
wild_animals =["Loner", "Loner Papa", "Loner Papa Again"]
animals.update(wild_animals, {"Loner Papas"})
print(animals)  

# Removing items in a set (using the discard or remove method)
animals.remove("cat")
print(animals)

'''
the difference between discard and remove is that if you try discarding an element that is not in the set, it'll return none, whereas remove returns an error
'''

# Removing all items in a set using the clear method
animal.clear()
print(animal)

# To check if an item is in a set or not
print("tiger" in animals) # true cuz tiger is in the set of animals

print(" ")
print(" ")
print(" ")
print(" ")

# Can also loop through
for animal in animals:
    print(animal)
    

# * PYTHON SET OPERATIONS
"""
- Union Set: this is a set of all items of two or more sets
- Intersection: this is a set that contains items that are common in different sets too. It's basically like that maths shit
"""

print(" ")
print(" ")
print(" ")

#? UNION SET
wild_animals = {"Loner", "Loner Papa", "Loner Papa Again"}
domesic_animals = {"Monkey", "Parrot", "Rabbit"}
# all_animals = wild_animals.union(domesic_animals)
# print(all_animals)
# OR use |
all_animals = wild_animals | domesic_animals 
print(all_animals)

#? INTERSECTION
wild_animals = {"Loner", "Loner Papa", "Loner Papa Again", "Monkey"}
domesic_animals = {"Monkey", "Parrot", "Rabbit", "Loner"}
# all_animals = wild_animals.intersection(domesic_animals)

# OR USE & 
all_animals = wild_animals & domesic_animals
print(all_animals)