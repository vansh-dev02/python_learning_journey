# File Handling in Python

file=open("my_data.txt", "r")
data=file.read()

print("Data of the file is: ", data)



with open("newtextfile.txt","r") as a:
    line1=a.readline()
    line2=a.readline()
    line3=a.readline()
    print("Line 1: ", line1)
    print("Line 2: ", line2)
    print("Line 3: ", line3)
    readLinesMethod= a.readlines()
    print(readLinesMethod)


