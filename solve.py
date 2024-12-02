def solve():
    safe = 0
    with open('input.txt') as f:
        for line in f:
            split_line = line.split(" ")
            is_increasing = all(int(i) <= int(j) for i, j in zip(split_line, split_line[1:]))
            is_decreasing = all(int(i) >= int(j) for i, j in zip(split_line, split_line[1:]))

            if is_increasing or is_decreasing:
                is_safe = all(abs((int(i) - int(j))) > 0 and abs((int(i) - int(j))) < 4 for i, j in zip(split_line, split_line[1:]))
                safe += 1 if is_safe else 0

    return safe

print(solve())