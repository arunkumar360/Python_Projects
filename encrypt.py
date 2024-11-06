import random
import string

chars = ' ' + string.digits + string.ascii_letters + string.punctuation

chars = list(chars)

key = chars.copy()

random.shuffle(key)

#Encrypt

plain_text = input("Enter your text to encrypt: ")
cipher = ''
for letter in plain_text:
    index = chars.index(letter)
    cipher += key[index]

print(f'Message is : {plain_text}')
print(f'Encrypted message is : {cipher}')

#Decrypt

cipher = input("Enter your text to decrypt: ")
plain_text = ''
for letter in cipher:
    index = key.index(letter)
    plain_text += chars[index]

print(f'Encrypted Message : {cipher}')
print(f'Message is : {plain_text}')




