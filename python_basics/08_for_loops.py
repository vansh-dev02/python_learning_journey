foodList=["cake", "Mango", "pizza"]

for item in foodList:
    print(item)


collegesTuple=("VIPS", "MAIT", "MSIT", "USICT")

for eachItem in collegesTuple:
    print("Top IPU colleges: ", eachItem)


#Range
#(start, stop, step)

for item in range (2, 21, 2):
    print(item)




#Break
for num in range (1,10,1):
    if num == 5:
        break
    print(num)


#Pass

for a in range (1,11,1):
    pass



#Continue

for b in range (1,6,1):
    if b == 3:
        continue
    print(b)

    