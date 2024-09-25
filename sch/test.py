# import random
# sample = random.randint(10000, 99999)
# print(f'22{sample}')

# import time
# tt = time.strftime('%y',)
# print(tt)

# print(time.gmtime())

# print('Hello!')

# import hashlib
# import os

# salt = input('Enter password: ')
# password = salt.encode('utf-8')
# # salt  = os.urandom(16)


# hashed_password = hashlib.sha256(password).hexdigest()

# unhashed_password = hashlib.sha256(password).hexdigest()

# print(f'''
#         Salt: {salt}
#         Password: {password}
#         SHA-256 Hashed password: {hashed_password}
# ''')

# if hashed_password == salt:
#     print("Logged In")
# else:
#     print('error')


import bcrypt

pwd = input('password: ')
password = pwd.encode('utf-8')

hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

print(f'Hashed Password: {hashed_password}')

login = input('Password: ')
login_pwd = login.encode('utf-8')

if bcrypt.checkpw(login_pwd, hashed_password):
    print('Correct!')
else:
    print('Error!')