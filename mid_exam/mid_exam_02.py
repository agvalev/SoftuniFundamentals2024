names_frends = input().split(', ')
blacklisted_friends = []
blacklisted_names = 0
lost_names = 0
list_whit_friends = names_frends
while True:
    command = input().split()
    if command[0] == "Report":
        print(f"Blacklisted names: {blacklisted_names}")
        print(f"Lost names: {lost_names}")
        print(f"{' '.join(names_frends)}")
        break

    if command[0] == "Blacklist":
        name = command[1]
        if name in names_frends:
            i_finded_name = names_frends.index(name)
            names_frends[i_finded_name] = "Blacklisted"
            blacklisted_friends.append(name)
            blacklisted_names += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    elif command[0] == "Error":
        index = command[1]
        index = int(index)
        if index <= len(names_frends) - 1 and index >= -1 and names_frends[index] != "Blacklisted" and names_frends[index] != 'Lost' :
            name_error_saved = names_frends[index]
            names_frends[index] = "Lost"
            lost_names += 1
            print(f"{name_error_saved} was lost due to an error.")
        else:
            continue
    elif command[0] == "Change":
        index_change = command[1]
        index_change = int(index_change)
        new_name = command[2]
        if index_change <= len(names_frends) - 1 and index_change > -1:
            name_change_saved = names_frends[index_change]
            # poped = names_frends.pop(index_change)

            names_frends[index_change] = new_name

            print(f"{name_change_saved} changed his username to {new_name}.")


