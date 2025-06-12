# class SampleClass:
#     num = 100
#
#     def getData(self):
#         print("Method called for the execution")
#
# obj = SampleClass()
# print(obj.num)
# obj.getData()

class Calculator:
    num = 100

    def __init__(self, a, b):
        print("Constructor called for execution")
        self.firstNmuber = a
        self.secondNumber = b

    def getData(self):
        print("Method called for the execution")
        return self.firstNmuber + self.secondNumber + self.num

obj = Calculator(4, 6)
print(obj.num)
obj.getData()
print(obj.getData())


