import pandas as pd
import numpy as np
import hashlib as hs

df = pd.DataFrame(['1c4b91d7483d11432181ab041bae4c382715377e70b3353a90a5aafea7ab1814','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'],
     index=['sudipto', 'rudranil'],
     columns=['password'])
df.loc['sudipto']['password']
#df2 = pd.DataFrame([], index=[])

directory = {}

while True:
    username = input("Enter your username")
    password = input("Enter your profile password or 0 to exit")
    p1 = hs.sha256(password.encode("ascii")).hexdigest()
    if p1=="5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9":
        break
    while p1 == df.loc[username]['password']:
        request=input("Enter 1 for read and 2 for write or 0 to exit")
        if request == '1':
            print(directory)
            break
        elif request == '2':
            web=input('Enter Website name')
            user=input('Enter user name')
            pass1=input('Enter password')
            directory[web]=(user,pass1)
            print(directory)
            break
        elif request=="0":
            break
    
    else:
        print('Wrong username password')
