#For loop

objList = [2, 3, 4, 5, 6, 7]
for j in objList:
    print(j*2)

print("************* sum of 10 natural numbers***************")
sumValue= 0
for i in range(1,9): #it will iterate loop start from 1 to i-1
    sumValue = sumValue+i
print("Sum of natural no is",sumValue)

print("************* adding iteration***************")
for a in range(1,9,3): # (start,end,iterateion)
    print(a)
print("*******Skipping starting postion************")
for b in range(10):
    print(b)