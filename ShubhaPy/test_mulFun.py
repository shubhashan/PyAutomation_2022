import pytest




@pytest.mark.usefixtures("setup")
class TestClass:

    def test_fixture1(self):
        print("Inside demo1")

    def test_fixture2(self):
        print("Inside demo2")

    def test_fixture3(self):
        print("Inside demo3")

@pytest.mark.usefixtures("ClassFix")
class TestClass1:

    def test_fixture11(self):
        print("Inside CF11")

    def test_fixture21(self):
        print("Inside CF21")

    def test_fixture31(self):
        print("Inside CF31")