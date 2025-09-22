import mysql.connector
from utilities.configurations import *

#Host - server , database , username, password
# con = mysql.connector.connect(host='localhost',database='APIDevelop',user='root',password='Learn@2025')
# print(con.is_connected())
# #
# cursor_Obj= con.cursor()
# cursor_Obj.execute('select * from CustomerInfo')
# # print(cursor_Obj.fetchone())
# #
# # #Fetchfirstrow
# # row= cursor_Obj.fetchone()
# # print(row)
# # print(row[3])
# # print(cursor_Obj.fetchone())
#
# #Fetchall rows
# allrows= cursor_Obj.fetchall()
# print(allrows)
# sum =0
# for row in allrows:
#     sum = sum + row[2]
# print(sum)
# assert sum == 340


#Using utility and passing values to execute query

con = getConnection()
#
cursor_Obj= con.cursor()
cursor_Obj.execute('select * from CustomerInfo')
# print(cursor_Obj.fetchone())
#
# #Fetchfirstrow
# row= cursor_Obj.fetchone()
# print(row)
# print(row[3])
# print(cursor_Obj.fetchone())

#Fetchall rows
allrows= cursor_Obj.fetchall()
print(allrows)
sum =0
for row in allrows:
    sum = sum + row[2]
print(sum)
assert sum == 340

query="update customerInfo set Location = %s where CourseName = %s"
data=('London','Jmeter')
cursor_Obj.execute(query,data)
con.commit()

cursor_Obj.execute('select * from customerInfo')
print(cursor_Obj.fetchall())

query = "delete from customerInfo where courseName = %s"
data1 = ('Jmeter',)
cursor_Obj.execute(query,data1)
cursor_Obj.execute('select * from customerInfo')
print(cursor_Obj.fetchall())

con.close()



