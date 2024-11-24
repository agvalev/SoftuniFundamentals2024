text = input()
encrypet_text = ""
for character in text:
    encrypted_charachter = chr(ord(character) + 3)
    encrypet_text+=encrypted_charachter

print(encrypet_text)