#WAP that takes input from user and print middle 3 char and last 2 in output

str2=input("What is your favourite food?: ")
mid= len(str2)//2
output1= str2[mid-1:mid+2]
print("The middle the char are:", output1)

output2= str2[-2:]
print("The last 2 char are: ", output2)




#WAP that takes sentence as input converts it into lower case replaces all space" " with "_"
#and print the new string

str=input("Tell us your name: ")
str1=str.lower()
print(str1)

str2=str1.replace(" ", "_")
print(str2)





#WAP that takes input then print first, last and total char

str3=input("What is your favourite color: ")
print("The first char is: ", str3[0:1])
print("The last char is: ", str3[-1:])
print("The total no. of char are: ", len(str3))

