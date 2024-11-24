def palindrome_function(list):
    result = ""
    for num in list:
        if str(num) == str(num)[::-1]:
            result += "True\n"
        else:
            result += "False\n"

    return result


list_of_palindroms = list(map(int, input().split(", ")))
print(palindrome_function(list_of_palindroms))
