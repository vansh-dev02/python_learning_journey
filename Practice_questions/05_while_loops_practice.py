#WAP to print numbers from 1 to 10

i=1
while i<=10:
    print(i)
    i=i+1

print("Ques-1 completed")




#WAP to print numbers from 10 to 1

j=10
while j>=1:
    print(j)
    j=j-1
    print("j =",j)
print("Ques-2 completed")




#WAP to print all even num between 1 and 50

n=1
while n<=50:
    if(n%2==0):
        print(n)
    n=n+1
print("Ques-3 completed")




#WAP that prints sum of first n natural numbers

m=int(input("Enter the number: "))
sum=0
while m>=1:
    sum=sum+m
    m=m-1

print("Sum: ", sum)
print("Ques-4 completed")





#WAP to print pattern

a=1

while a<=4:
    print("*"*a)
    a=a+1
print("Ques-5 completed")




#WAP to print name with number in front

goodname=input("Please tell your name: ")
b=int(input("Enter the number of times you want your name to be printed: "))
c=1
while c<=b:
    print(f"{c}.{goodname}")
    c=c+1

print("Ques-6 completed")




#WAP to write multiplication table of any number

multiply=int(input("Write the number to get it's table: "))
d=1
while d<=10:
    print(f"{multiply}*{d}={d*multiply}")
    d=d+1
print("Ques-7 completed")

