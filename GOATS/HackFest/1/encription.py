from cryptography.fernet import Fernet

key = open("key.key", "rb").read()
message = str(open("message.txt", "r").read())

f = Fernet(key)
x = f.encrypt(message.encode())
print(x)

