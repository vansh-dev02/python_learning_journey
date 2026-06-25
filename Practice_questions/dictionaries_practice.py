#Create a dictionary named marks to store marks of 3 subjects
#Add the subjects one by one and print the final dictionary

marks={}
print(type(marks))
marks["Maths"]= 82
marks["Chemistry"]= 89
marks["Physics"]= 71


print(marks)






#Create list pf food items
#Convert list to set and print length and set


food=["Rajma","Chole","Pao Bhaji", "Rajma", "Bhindi"]
print(type(food))
#How to convert list to set

food=set(food)
print(type(food))

print("The total number of foods are: ", len(food))
print(food)




#Create a dictionary storing meanings of 3 english words

words={
    "Fluke":"Tukka",
    "Alacrity":"Cheerful willingness",
    "Tenacious":"Persistant and determined"
}

print("Three english words with meanings are: ", words)








#Create a set of numbers and show union and intersection with another set

set1={1,2,5,6}
set2={1,3,4,6}
print("Union of 2 sets is: ", set1.union(set2))
print("Intersection of both sets is: ", set1.intersection(set2))

