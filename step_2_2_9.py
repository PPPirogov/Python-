from simplecrypt import decrypt

with open("../good_connect/encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "rb") as pas:
    password = pas.read()
s = password.decode('UTF-8')
passwords = s.split('\n')
# print(encrypted)
print(passwords)
answer=[]
for a in passwords:
    try :
        b = (decrypt(a, encrypted).decode('utf8'))
        print(b)
    except:
        print('error')

