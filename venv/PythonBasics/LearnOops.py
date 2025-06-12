from PythonBasics.classDemo import Calculator

class SampleInhertiance(Calculator):
    num2 = 300

    def __init__(self):
        Calculator.__init__(self,5,9)

    def getCompleteData(self):
        print("All values are here")
        return self.firstNmuber + self.secondNumber + self.num +self.num2


odj = SampleInhertiance()
print(odj.num2)
print(odj.getCompleteData())