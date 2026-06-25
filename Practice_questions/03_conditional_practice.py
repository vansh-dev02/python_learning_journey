#Take number as input and tell if postive negative or zero

num=int(input("Please enter a number"))

if(num>0):
    print("The number entered is positive\nThankyou!")
elif(num==0):
    print("The number entered is zero itself\nThankyou!")
elif(num<0):
    print("The number entered is negative\nThankyou!")




#WAP that take 3 food store in list print list and it's length
food1=input("Enter food 1: ")
food2=input("Enter food 2: ")
food3=input("Enter food 3: ")

foodlist=[]
foodlist.append(food1)
foodlist.append(food2)
foodlist.append(food3)

print(foodlist)
print(len(foodlist))





#WAP That take tuple of 5 fav fruits 
#Print total no. of fruits
#Print index of one selected fruit

fruit1=input("Enter fruit 1: ")
fruit2=input("Enter fruit 2: ")
fruit3=input("Enter fruit 3: ")
fruit4=input("Enter fruit 4: ")
fruit5=input("Enter fruit 5: ")

fruitTuple=(fruit1, fruit2, fruit3, fruit4, fruit5)

print(fruitTuple)
print(len(fruitTuple))

print("The index of Apple is: ", fruitTuple.index("Apple"))









