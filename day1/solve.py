left_list = []
right_list = []
total_dist = 0

def insert_sorted(list, item):
    i = 0
    if not list or item > list[-1]:
        list.append(item)
    else:
        while item > list[i] and i < len(list):
            i += 1
        list.insert(i, item)

with open('input.txt') as f:
    for line in f:
        split_line = line.split("   ")
        left_int = int(split_line[0])
        right_int = int(split_line[1])
        insert_sorted(left_list, left_int)
        insert_sorted(right_list, right_int)

for i in range(len(left_list)):
    dist = abs(left_list[i] - right_list[i])
    total_dist += dist

print(total_dist)
