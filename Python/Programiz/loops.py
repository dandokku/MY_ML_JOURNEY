# WHILE LOOP
'''
while test_condition:
    statement(s)
'''

count = 0
print(count)
while count < 5:
    count += 1
    print(count)
    

# Exercise1
# number = int(input("Enter a number"))
# count = 1
# while count <= 12:
#     product = number * count
#     print(number, "x", count, "=", product )
#     count += 1 
    

# Exercise2
# number = int(input("Enter a number: "))
# count = 12
# while count >= 1:
#     product = number * count
#     print(number, "x", count, "=", product)
#     count -= 1


#* FOR LOOPS
#note: a sequence is a collection of items in an order

# for loop is used to iterate over a sequence an in each each iteration, we can access each of the items in the sequence
'''
for item in sequence:
    statement(s)
'''

text = "Dandokku"

for t in text:
    print(t)


languages = ["English", "French", "German", "Dandokku"]

for language in languages:
    print(language)
    
# RANGE
count = 1
while count <= 5:
    print(count)
    count = count + 1 
#! OR
print(" ")

for count in range(1, 6):
    print(count)
    
print("     ")    
# Exercise 1
# number = int(input("Enter a number: "))

# for count in range(1, 11):
#     product = number * count
#     print(number, "x", count, "=", product)
    
# Exercise 2
total = 0
for x in range(1, 101):
    total += x
    print("Adding", x, "gives a total of:", total)
print("The final sum of numbers from 1 to 100 is:", total)
