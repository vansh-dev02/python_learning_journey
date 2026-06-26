#WAP that prints welcome to python programming 3 times


def welcome_message():
    print("Welcome to python programming!")

welcome_message()
welcome_message()
welcome_message()




#Print name and age

def show_age(name="Vansh", age=25):
    print(f"{name} is {age} years old")

show_age("Vansh", 19)
show_age()
show_age("Hardik", 18)




#print sum and diff

def add_numbers(a,b):
    sum=a+b
    difference=a-b
    print("Sum of 2 numbers is: ", sum)
    print("Difference of 2 numbers is: ", difference)


add_numbers(4,5)
add_numbers(3,78)





#WAP that returns square of a number

def square(num):
    return num**2

print(square(2))
print(square(12))




#WAP that takes a string and returns count of vowels and consonants

def countVowConso(userInput):
    vowels = "aeiouAEIO"

    countvowel = 0
    countconsonants = 0

    for eachchar in userInput:
        if eachchar.isalpha():
            if eachchar in vowels:
                countvowel += 1
            else:
                countconsonants += 1

    return countvowel, countconsonants


vowels, consonants = countVowConso("Vansh Chhabra")

print("\nVowels:", vowels)
print("\nConsonants:", consonants)







