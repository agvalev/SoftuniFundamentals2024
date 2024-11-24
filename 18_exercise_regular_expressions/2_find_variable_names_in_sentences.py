import re
sentence = input()

regex = r"\b_([A-Za-z0-9]+)\b"

variables = re.findall(regex, sentence)

print(",".join(variables))