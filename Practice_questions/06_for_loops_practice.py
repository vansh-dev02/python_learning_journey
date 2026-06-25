#WAP to prevent even numbers between 1 and 20

for i in range(2,21,2):
    print("Even numbers in range: ", i)
print("Ques-1 completed\n")



#WAP to print num 1 to 50 but print "Vansh" instead of numbers that are multiple of 5

for num in range(1,51,1):
    if(num%5==0):
        print("Vansh")
    else:
        print(num)
print("Ques-2 completed\n")



#WAP to print square of each number from 1 to 10

for square in range (1, 11, 1):
    print(f"{square}*{square}={square*square}")
print("Ques-3 completed\n")



#WAP take input number and print table

multiply=int(input("Enter the number: "))

for a in range (1,11,1):
    print(f"{multiply}*{a}={multiply*a}")
print("Ques-4 completed\n")




#WAP that prints numbers from 100 to 1

for b in range (100, 0, -1):
    print(b)
print("Ques-5 completed\n")





#WAP that prints username in uppercase 10 times
username=str(input("Please tell your username: "))
for d in range (1, 11):
    print(f"{d}.{username.upper()}")

print("Ques-6 completed\n")



