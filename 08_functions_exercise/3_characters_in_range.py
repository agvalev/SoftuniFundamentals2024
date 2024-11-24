def chars_range(first_char, second_char):
    result = ""

    for i in range(ord(first_char) + 1, ord(second_char)):
        result += chr(i) + " "

    return result


char_1 = input()
char_2 = input()

print(chars_range(char_1, char_2))
