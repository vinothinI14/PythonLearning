import pytest

@pytest.mark.smoke
def test_firstTestMethod():
    print("Happy to learn pytest")

@pytest.mark.xfail
def test_creditCardTest():
    a = 10
    b = 100
    print(a+b)