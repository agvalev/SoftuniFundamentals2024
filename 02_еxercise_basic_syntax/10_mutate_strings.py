first_string = input()
second_string = input()
last_printet_string = first_string
for charachter_index in range(len(first_string)):
    left_part = second_string[:charachter_index +1]
    right_part = first_string[charachter_index +1:]
    new_string = left_part + right_part
    if new_string != last_printet_string:
        print(new_string)
        last_printet_string = new_string
# ako ne mojesh da go proumeesh gledaj basic_syntax_exersice 9:52
#ostavashti
# [start:stop:step] - 4:10