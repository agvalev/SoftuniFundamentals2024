count_of_targets = 0
data = list(map(int, input().split()))
list_with_targets = data
while True:
    command = input()
    if command == "End":
        break
    index = int(command)
    if 0 <= index < len(list_with_targets) and list_with_targets[index] != -1:
        count_of_targets += 1
        special_value = list_with_targets[index] # tozi red pravi promenliva v koqto durjim targeta s kojto rabotim v momenta predi da go napravim na -1 za da mojem
        #sled tova da go izvadim ili suberem s ostanalite
        list_with_targets[index] = -1 # tova vseki put minava i pravi ot lista mi indeksa kojto e na -1 zashtoto veche e strelqno
        for i in range(len(list_with_targets)):
            if list_with_targets[i] == -1:
                continue
            if special_value <= list_with_targets[i]:
                list_with_targets[i] -= special_value
            else:
                list_with_targets[i] += special_value

convert_target_values_string = [str(num) for num in list_with_targets]
print(f"Shot targets: {count_of_targets} -> {' '.join(convert_target_values_string)}")
