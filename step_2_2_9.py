from simplecrypt import encrypt, decrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
with open("passwords.txt", "rb") as inp:
    password = inp.read()
s = password.decode('UTF-8')
passwords = s.split('\n')
# print(encrypted)
# print(passwords)
answer=[]
for a in passwords:
    answer.append(decrypt(a,encrypted))