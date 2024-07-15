from cryptography.fernet import Fernet

with open("mykey.key", "rb") as mykey:
    key = mykey.read()

print(key)

f = Fernet(key)    

with open("list.csv", "rb") as original_file:
    original = original_file.read()


encrypted = f.encrypt(original)

with open("enc_list.csv", "wb") as encrypted_file:
    encrypted_file.write(encrypted) 