number_of_words = int(input())
sinonims = {}
for word in range(number_of_words):
    current_word = input()
    synonim = input()
    if current_word not in sinonims.keys():
        sinonims[current_word] = []
    sinonims[current_word].append(synonim)
for word, list_of_sinonims in sinonims.items():
    print(f"{word} - {', '.join(list_of_sinonims)}")