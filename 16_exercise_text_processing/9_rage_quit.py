text = input()
rage_message = ""
repetisions = ""
current_symbol = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index].upper()
    else:
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetisions += text[next_symbols]
        rage_message += current_symbol * int(repetisions)
        repetisions = ""
        current_symbol = ""

print(f"Unique symbols used: {len(set(rage_message))}") # broq na unikalnite simvoli v lista
print(rage_message)
