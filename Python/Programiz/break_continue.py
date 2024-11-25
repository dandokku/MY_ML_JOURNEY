for i in range(1,6):
    print(i)
    if i == 3:
        break
    
names = ["Kami", "Dandokku", "Haiteku", "Welo", "Samuel", "Daniel"]

for name in names:
    print(name)
    if name == "Haiteku":
        break

print(" ")
# Exercise 1
languages = ["Python", "Java", "Swift", "C", "C++"]
for language in languages:
    if language == "Swift" or language == "C++":
        continue
    else:
        print(language)
    