def is_paliandrome(s):
    return s == s[::-1]

times_founded_paliandrom = 0
words = input().split()
paliandrom = input()
list_pal = []
for word in words:
    if is_paliandrome(word):
        list_pal.append(word)

    if paliandrom in word:
        times_founded_paliandrom +=1

print(list_pal)
print(f"Found palindrome {times_founded_paliandrom} times")