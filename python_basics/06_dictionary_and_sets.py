#Dictionary in Python
#Inside Curly braces

student = {
    "name": "Vansh Chhabra",
    "age": 19,
    "city": "Sonipat",
}

# name, age, city are KEYS

print(type(student))
print(student)
print(student["name"])
print(student["city"])
student["city"]="Delhi"
print(student)
student["FavSubject"]="Maths"
print(student)


#Removing item
student.pop("FavSubject")
print(student)

print(student.keys())
print(student.values())
print(student.items())



# Sets in Python

languages={"Python", "Java", "C++", "Python"}
print(type(languages))
print(languages)

#Sets do not entertain duplicacy

emptySet=set()
print(type(emptySet))

languages.add("C")
languages.add("Javascript")
print(languages)
languages.remove("C")
print(languages)




