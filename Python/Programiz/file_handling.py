'''
r(read mode) - opens a file for reading(default)

w(write mode) - opens a file for writing, creates a new file if it doesn't exist, clears the content of the file if it exists

a(append mode) - opens a file for appending at the end of the file, creates a new file if it doesn't exist
'''
try:
    f = open("Python\Programiz\welp.txt", "r")

    # Reading the contents of the file
    content = f.read(2)
    content2 = f.read(10) # only the first 10 characters in the file will be read
    print(content)
    print(content2)
finally:
    f.close()
    
# ! another way to oopen
with open("Python\Programiz\welp.txt") as f:
    content = f.read(2)
    content2 = f.read(10) # only the first 10 characters in the file will be read
    print(content)
    print(content2)
    
    

# * Writing Files
'''
- If a file doesn't exist, a new file is created
- If the file already exists, it's overwritten
'''

with open("Python\Programiz\omo.txt", "w") as f:
    f.write("Omo, this is fun" )