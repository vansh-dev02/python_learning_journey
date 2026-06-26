#Personal Expense Tracker

expenses = [ ] #List of all expenses in form of dictionary

print("Welcome to Expense Tracker : ")

while True:
    print("===MENU===")
    print("1. Add Expense: ")
    print("2. View All Expense: ")
    print("3. View Total Expenses: ")
    print("4. Exit")

    choice = int(input("Pleas enter your choice(1-4): "))


#ADD EXPENSE
    if(choice==1):
        date=input("Enter the date of expense: ")
        category=input("Enter the category: ")
        description=input("Describe your expense: ")
        amount=float(input("Enter the Total Amount: "))

        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount
        }

        expenses.append(expense)
        print("\n DONE. Expense is added successfully")



    #2. View all expenses
    if(choice == 2):
        if(len(expenses)==0):
            print("NO EXPENSE ADDED")
        else:
            print("===This is all the expense===")
            count = 1


            for eachExpense in expenses:
                print(f"Expense number {count} -> {eachExpense["Date"]}, {eachExpense["Category"]}, {eachExpense["Description"]}, {eachExpense["Amount"]} ")
                count = count+1



    #3. View Total Expense

    if (choice == 3):
        total=0
        for eachExpense in expenses:
            total =  total +eachExpense["Amount"]
        print("TOTAL EXPENSE = ", total)



    #4. Exit
    elif(choice == 4):
        print("Thankyou for using! ")
        break

    

