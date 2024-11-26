# A list is a sequence of items in an order

# A list of integers
numbers = [1, 3, 9, 5, 8,]
print(numbers)

# Mixed list
random_list = [2.5, "welp", True, -1, 29]
print(random_list)

# Empty or Null List
list1 = []
print(len(list1)) #! the size of an empty list is 0

languages = ["Python", "Javascript", "C++", "Kotlin"]
print(languages)
print(languages[2]) #! Indexes are used to access items in a list, and the index always starts from 0
print(languages[-2]) #! you can also access items on the list starting from the back
print(languages[0:3]) #! this prints all the items from the first to the third
print(languages[:3]) #! still the same as the former
print(languages[2:]) #! prints everything in the list starting from the specified index

# You can also change the items in a list  using the index
languages[2] = "Flutter"
print(languages)
languages[0:2] = ["Dart", "PhP"]
print(languages)

# Iterating through a list
print("Rust" in languages) #! this returns false because Rust doesn't exist in the list.

# Adding items to a list
languages.append("Rust")
print(languages)

languages.insert(1, "C#") #! the index and the value
print(languages)



# TUPLES
# unlike lists, you can't change anything in a tuple, and it's unordered
numbers = (21, -5, 6, 9)
print(numbers)
print(numbers[2])
print(numbers[1:3])

#! You can't add or remove from a tuple
# numbers[0] = 2
# print(numbers) 

'''
SUMMARY:
- A list is a collection of ordered items
- To access individual elements of a list, we use indices
- To access a portion of a list, we use the slicing operator(1:2 kinda shii)
- Python has several useful methods that make it easier to add, change, insert and remove list elements
- A tuple is similar to a list except tuples are immutable, we cannot change elements of a tuple
'''

