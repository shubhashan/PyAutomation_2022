class Student:
    course = "BE"  # class variable
    count = 0

    def __init__(self, name, id):  # instance method starts with self
        self.name = name  # instance variables
        self.id = id
        Student.count = Student.count + 1

    @classmethod
    def countobj(cls): #class method
        return cls.count

    @staticmethod
    def branch(branch):
        if branch == "CS" or branch == "IT":
            print("Computer Engg")
        else:
            print("Other Engg branches")

s3 = Student('Akriti', 20)
s1 = Student('John', 10)
s2 = Student('Akriti', 20)
print(s1.id)
print(s1.name)
print(s1.course)
print(s2.id)
print(s2.name)
print(s2.course)
print(Student.countobj())
print(s3.countobj()) #you can call class method using object as well
s3.branch("CS")
s1.branch("EC")
Student.branch("IT") #you can call staticmethod using class also


def displayAllCustInfo(self):
    rows = self.noOfRows()
    cols = self.noOfColumns()
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cell = "//table[@id='customers-grid']//tbody//tr[" + str(i) + "]//td[" + str(j) + "]"
            print(cell, end='')