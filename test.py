import numpy as np
import pandas as pd
from datetime import datetime


# before = datetime.now()
# for i in range(100000000):
#     continue
# after = datetime.now()
#
# print(after-before)


import bcrypt
def Encrypt(p):

    #Got the bcrypt idea from this youtube video https://www.youtube.com/watch?v=CSHx6eCkmv0
    passwd = bytes(p,encoding='UTF-8')

    salt = bcrypt.gensalt() # this generates a random string to be appended to the end of password and hashpw will hash both of these strings
    hashed = bcrypt.hashpw(passwd, salt)
    return hashed

hashed = Encrypt('hello')

if bcrypt.checkpw(b'hello', hashed): # checkpw will decrypt it and then return
    print("match")
else:
    print("does not match")
