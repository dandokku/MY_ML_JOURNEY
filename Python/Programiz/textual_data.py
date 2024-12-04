# A string is a sequence of characters

text =  "Hello There" # This is a string, because it is enclosed inside a quote
text2 = 'Welp' # Also a string, you can also use single qoutes
text3 = """Omo, Dandokku""" # Can also use triple quote

text4 = "He said, \"What\'s there?\""
print(text4)
print(text[2]) # can access characters this way
print(text[-2]) # strings also supports negative indexing
print(text[1:4]) # yeah you can also do this, though note that the first index is included but the last is not(just like list and arrays)

''' Strings in python are immutable, You can not change characters in a string. 
Though there are numbers of operations that can be performed on strings
'''
join_text = text + " " + text2
print(join_text)

repeat_text = text * 5
print(repeat_text)

# Can also loop through a string
for character in text:
    print(character)
    
# You can also check if a character is in a string
print("Hello" in text) # returns True cuz there is Hello in text
# but hold up, is it case sensitive?
print("hello" in text) # yes it is case sensitive
# how about this
# print(text.lower("Hello") in text) # that is ass code, never do that again

quote = "Talk is cheap, Show me the code."
print(quote[3])
print(quote[-3])
print(quote.replace("code", "program"))