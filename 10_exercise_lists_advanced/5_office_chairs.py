def check_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_room, visitors = input().split()
        difference = len(free_chairs_in_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs



count_of_rooms = int(input())
total_free_chairs = check_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")