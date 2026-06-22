#Ways to add string

str1= "Hello"
str2= 'Hello Programming'
str3= '''Hello Vansh'''

print("Hello"+"World")


#Length of string

print(len(str1))
print(len(str2))
print(len(str3))


#Indexing
#starts from 0 character

str4="programming"
print(str4[4])
print(len(str4))
print(str4[5])
print(str4[0])


#Slicing
#Let's you access part of a string

str="Gulabjamun"
print(str[0:5]) #gulab
print(str[:6]) #gulabj
print(str[5:]) #jamun


#Common string methods

str5="vansh chhabra"
print(str5.upper())
print(str5.lower())
print(str5.title())
print(str5.find("hh"))
print(str5.replace("vansh", "Mr."))
print(str5.count("a"))


#f-strings

name ="Vansh Chhabra"
age= 20
print(f"My name is {name} and my age is {age}")


#escape sequences
#\n
#\\
#\'
#\""

print("Hellow world")
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print("Hello\'World")
print("Hello\"World")








