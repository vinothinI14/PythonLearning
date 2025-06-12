file = open('C:/Users/ADMIN/PycharmProjects/LearningPython/venv/SampleData/TestFile.txt')

#print(file.read()) #Read data fron file

#print(file.readline()) #Readline concept in python

#Readlines in python
# lines = file.readlines()
# for line in lines:
#     print(line)

#File open using with

fileName = 'C:/Users/ADMIN/PycharmProjects/LearningPython/venv/SampleData/TestFile.txt'
# with open(fileName, 'r') as reader:
#     print(file.read())

reves = reversed(file.readlines())
with open(fileName,'w') as writer:
    for rev in reves:
        writer.write(rev)