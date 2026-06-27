# WAP to read a text from a given file
# and find
# if it contains word live

file = open("certificate.txt", "r")
dataOfFile= file.read()

dataOfFile=dataOfFile.lower()

if "live" in dataOfFile:
    print("Yes Live word is present in the file")
else:
    print("No Live word is not present in the file")
print("Ques-1 completed")
file.close()
#If file non existing no such file existing





# Open a file in write mode

file=open("report.text", "a")
file.write("I am learning python very well and it's great learning new things")
file.write("\nALL SET")
file.close()




#Read first line of file and print total lines
with open("newfile.txt","r") as b:
    listOfLines=b.readlines()
    print("Total lines are: ", len(listOfLines))
    print(listOfLines)










