import csv


with open("utilities/Data/SampleTest.csv") as csvRead:
    data = csv.reader(csvRead,delimiter =',')
    print(type(data))
    print(data)
    names=[],status=[]
    for row in data:
        names.append(row[0])
        status.append(row[1])
print(names)
print(status)

#Write into csv file

with open("utilities/Data/SampleTest.csv", 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow("Four","Reg","Reg1","Reg2")