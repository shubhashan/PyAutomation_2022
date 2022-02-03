import random
import string
import time

'''
def randomG(size=10,chars=string.ascii_uppercase+string.ascii_lowercase+string.digits):
    print( ''.join(random.choice(chars) for x in range(size)))


randomG()
randomG()
randomG()
randomG()

'''


def randomG(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

E = randomG()
email = E + '@gmail.com'
print(email)
print("This __name__ is p.py    :     "+ __name__)


