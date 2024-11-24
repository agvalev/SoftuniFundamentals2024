def manipulate_dis(distance_list, sum_removed_elements, cur_index):
    removed_element = 0
    if cur_index < 0:
        removed_element = distance_list[0]
        distance_list[0] = distance_list[-1]
    elif cur_index >= len(distance_list):
        removed_element = distance_list[-1]
        distance_list[-1] = distance_list[0]
    else:
        removed_element = distance_list.pop(cur_index)
    sum_removed_elements += removed_element
    for manipulating_index in range(len(distance_list)):
        if distance_list[manipulating_index] <= removed_element:
            distance_list[manipulating_index] += removed_element
        else: #distance_list[manipulating_index] > removed_element:
            distance_list[manipulating_index] -= removed_element

    return distance_list, sum_removed_elements


distance = [int(number) for number in input().split()]
sum_of_removed_elements = 0
while distance:   #dokato imam neshto v distance(kogato nqmam nishto veche shte stane false i nqma da vleze)
    index = int(input())
    distance, sum_of_removed_elements = manipulate_dis(distance, sum_of_removed_elements, index)
print(sum_of_removed_elements)