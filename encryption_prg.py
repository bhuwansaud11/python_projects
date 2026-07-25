import string
import random

chars = " " + string.punctuation + string.ascii_letters+string.digits

chars = list(chars)

key = chars.copy()

random.shuffle(key)

#ENCRYPT

plain_text = input("Enter the messsage to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text+=key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPT

cipher_text = input("Enter the message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text+=chars[index]

print("Decrypted message: ",plain_text)