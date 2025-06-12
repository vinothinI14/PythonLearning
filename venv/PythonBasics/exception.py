# itemInCart = 0
#
# if itemInCart !=2:
#     raise("Item not matching")


#Try Except

try:
    with open('C:/Users/ADMIN/PycharmProjects/LearningPython/venv/SampleData/TestFile.txt') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("Finally block")