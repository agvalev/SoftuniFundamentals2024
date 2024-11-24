text = input()
final_text = ""
last_string = ""

for character in text:
    if character != last_string:
        final_text += character
        last_string = character
print(final_text)