# while True:
#     double_char = ""
#     string = input()
#     if string == "End":
#         break
#     if string == "SoftUni":
#         continue
#     for char in string:
#         double_char += char *2
#     print(double_char)
double_char = ""
string = input()
for char in string:
    double_char += char * 2
print(double_char)