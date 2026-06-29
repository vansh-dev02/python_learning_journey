# Create a class laptop with 3 attributes
#create 2 objects with diff values

class laptop:
    brand="default"
    RAM="8GB"
    price="1 lakh"

laptop1=laptop()
laptop1.brand="HP"
laptop1.RAM="16GB"


laptop2=laptop()
laptop2.brand="Lenovo"

print("1st Laptop brand: ", laptop1.brand)
print("2nd laptop brand: ", laptop2.brand)





#Create class student that takes 3 marks and has a method average()

class student:

    def __init__(self, name, listOfMarks):
        self.name=name
        self.listOfMarks=listOfMarks

    def average(self):
        sum=0
        for eachValue in self.listOfMarks:
            sum=sum+eachValue
        average=sum/3
        print("Average is: ", average)


student1=student("Vansh",[90, 98, 99])
student1.average()





#Create account with attribute balance and acc_number
#add methods debit,credit, print balamce


class account:
    def __init__(self, balance, acc_number):
        self.balance=balance
        self.acc_number=acc_number
    
    def credit(self, amount):
        self.balance=amount+self.balance
        print("Amount credited: ", amount)

    def debit(self, amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Amount debited: ", amount)
        else:
            print("Insufficient funds")

    def show_balance(self):
        print("Account: ", self.acc_number)
        print("Balance: ", self.balance)


a1=account(20000,"195200")
a1.credit(2000)
a1.debit(5000)
a1.show_balance()







#Create class child with name, section, marks with method get_percentage

class child:
    def __init__(self, name, section, marks):
        self.name=name
        self.section=section
        self.marks=marks
    def get_percentage(self):
        total_marks=sum(self.marks)
        percentage=total_marks/len(self.marks)
        return percentage


child1=child("Vansh","A", [80,90,78,94,89])
print("Name: ", child1.name)
print("Section: ", child1.section)
print("Percentage: ", child1.get_percentage(),"%")





