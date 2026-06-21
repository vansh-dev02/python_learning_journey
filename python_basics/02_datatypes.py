#Data types
food=("Samosa")
age=(20)
area=(60.45)
print("Datatype of food is:", type(food))
print("Datatype of age is:", type(age))
print("Datatype of area is :", type(area))

#Input 2 numbers and print their sum

a= int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum = a + b
print("The sum is:", sum)

#Type conversion

#implicit(automatic)
#x is int and y is float so sum is float 

x = 5 #int
y = 10.5 #float
z = x+y #float

print("Answer is:", z)
print(type(z))

#explicit(manual)

num=input("Enter value:")
converted_value= float(num)

print("Original value:",num, "Datatype:", type(num))
print("converted value:",converted_value, "Datatype:", type(converted_value))

