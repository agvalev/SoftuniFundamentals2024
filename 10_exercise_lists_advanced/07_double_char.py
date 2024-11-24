numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_cur_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_cur_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in current_group]
    #taka prezapisvam promenlivata s mahnatite grupi
