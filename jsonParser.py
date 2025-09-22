import json

#Loads used to parse string values
courses = {'name':'Vinothini','languages':['java','Python']}
json_string = json.dumps(courses)
data=json.loads(json_string)
print(type(data))
print(data['name'])
print(data['languages'])
print(data['languages'][1])

#Load method used to parse file object

with open("C:\\Users\ADMIN\\Desktop\\Vino_Doc\\Learning\\Course.json") as f:
    data = json.load(f)
    print(data['dashboard']['website'])
    for course in data['courses']:
        if course['title'] == "RPA":
            print(course['price'])
#Compare json
with open("C:\\Users\ADMIN\\Desktop\\Vino_Doc\\Learning\\Course2.json") as f1:
    data2=json.load(f1)
    assert data == data2
