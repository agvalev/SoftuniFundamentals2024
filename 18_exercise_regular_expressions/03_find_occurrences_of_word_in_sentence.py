import re

sentence = input()
serched_word = input()

pattern = fr"\b{serched_word}\b"
matches = re.findall(pattern,sentence, re.I)
print(len(matches))