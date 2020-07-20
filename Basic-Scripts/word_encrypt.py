import hashlib

input_word = input("Enter the word you want to encrypt: ")

hashed_input = hashlib.sha256(input_word.encode())

out_hash = hashed_input.hexdigest()

print(out_hash)