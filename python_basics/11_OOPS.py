# OOPS in Python
#Class creation

class vehicle:
    color="black"
    petrolORdiesel="Petrol"
    mileage="15"

    def start(): #Method
        print("When clutch is pressed engine is started")


#Object creation
car = vehicle()
print(car.color)

bike=vehicle()
print(bike.color)

aeroplane=vehicle()
print(aeroplane.mileage)

#Classes and Objects understood




#init is always called whenever a n object is created
#used to intialize attribute

class student:
    school="ABC school"
    def __init__(self, name, course):
        print("I am called automaticcally after object is created")
        self.name=name
        self.course=course
        print(self.name)
        print(self.course)

student1=student("Vansh", "Btech") #init called
student2=student("Hardik", "Btech")
print(student1.school)
print("Student 1 name: ", student1.name)
print("Student 2 name: ", student2.name)


#@staticmethod
#No need to add (self) 
