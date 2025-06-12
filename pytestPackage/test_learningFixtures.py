import pytest


@pytest.mark.usefixtures("setup","dataload","parameterization")
class Testsample:


    def test_samplemethod(self):
        print("I am part of this learning fixture")


    def test_samplemethod2(self,dataload):
        print("I am part of this learning fixture2")
        print(dataload[0],dataload[1],dataload[2],dataload[3])


    def test_samplemethod3(self,parameterization):
        print("I am part of this learning fixture3")