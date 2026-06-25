#Smart temperature converter
#Take input in celsius and write equivalent is farenheit and kelvin

celsius=float(input("Write temperatur in celsius:"))
farenheit=(celsius*9/5)+32
kelvin=(celsius+273.15)

print("Temperature in celsius is:", celsius)
print("Temperature in farenheit is:", farenheit)
print("Temperature in kelvin is:", kelvin)


#Bill split calculator
#Take total bill and no. of friends and calculate how much each person will pay 
#Also write the data type

Total = float(input("Enter the total bill amount:"))
friends = int(input("Enter total no. of friends:"))
bill = Total/friends

print("Each person will pay:", bill)

print("Datatype of total:", type(Total))
print("Datatype of friends:", type(friends))
print("Datatype of bill:", type(bill))


