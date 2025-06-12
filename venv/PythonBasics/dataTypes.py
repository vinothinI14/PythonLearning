#Numeric
#String
#List (Mutable)

values= [1, 5, "vino", 10, "welcome"]
print(values[2])
print(values[1:4]) #Print sub values
print(values[-1]) #Print last value fom list

values.insert(3,"Kandy") #Insert new value at particular index
print(values)

values.append("To my home") #Add new value at the end
print(values)

values[2]="VINO" #Update value in list
print(values)

del values[3]  #Delete value from the list
print(values)

#Tuple dame as list its immutable

val =(1, 4, "Vino" , 5, 0)
print(val)
print(val[-1])

#Dictionary

value ={1:"Vino", "Two":"Suvi", 3:"Sam"}
print(value[1])


#How to create dictionary at run time

dict = {}
dict["FirstName"] = "Vino"
dict["LastName"] = "Kandasamy"
dict["Gender"] = "Female"
print(dict)