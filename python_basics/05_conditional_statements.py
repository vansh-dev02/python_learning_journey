#conditional statements

marks=int(input("Please tell you marks out of 100: "))
if(marks>=90):
    print("Your grade is A")
elif(marks>=80):
    print("Your grade is B")

print("My code ends here")



#List in python
#To store multiple data

food = ["Dimsums", "Waffle", "Apple", "Mango", "Pineapple", "90"]
print(len(food))

print("First value of the list is: ", food[0])
print("Fourth value of the list is: ", food[3])


#Methods in Lists

Marks= [99, 100, 90, 95]
print(Marks)
Marks[1]= 98
print(Marks)

print(Marks[1:3])

print("Maximum marks are: ",max(Marks))
print("Minimum marks are: ",min(Marks))

Marks.append(92)
print(Marks)

Marks.sort()
print(Marks)





#Tuple in Python
#Cannot be changed like lists

studentTuple= ("Vansh", "Hardik", "Uttkarsh", "Vansh")

print(studentTuple[1])
print(type(studentTuple))


#Empty Tuple

emptyTuple=()
singleTuple= (1,) #without comma type=int
print(type(emptyTuple))
print(type(singleTuple))
print(studentTuple.index("Vansh"))
print(studentTuple.count("Vansh"))

