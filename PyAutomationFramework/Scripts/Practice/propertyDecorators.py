class fullname:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        return self.fname + "." + self.lname + "@gmail.com"

    @email.setter
    def email(self, msg):
        self.msg = msg
        d = msg.split(" ")
        self.fname=d[-2]
        self.lname=d[-1]
        #return email


P1 = fullname("John", "Smith")
print(P1.fname)
print(P1.lname)
print(P1.email)
P1.fname = "Arthur"
print(P1.fname)
print(P1.lname)
print(P1.email)

P1.lname = "Johnson"
print(P1.fname)
print(P1.lname)
print(P1.email)
P1.email = "Update name Arthur123 Smith"
print(P1.fname)
print(P1.lname)
print(P1.email)

