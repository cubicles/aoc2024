def part1():
    with open('input2.txt') as file:
        lines = [line.rstrip() for line in file]
    c = 0
    for line in lines:
        values = []
        numbers = line.split(' ')
        for n in numbers:
            values.append(int(n))

        decreasing = all((i > j and i - j <= 3) for i, j in zip(values, values[1:]))
        increasing = all((i < j and j - i <= 3) for i, j in zip(values, values[1:]))

        if (decreasing or increasing):
            c = c + 1
    print(c)

def part2():
    with open('input2.txt') as file:
        lines = [line.rstrip() for line in file]

    safe_list = []
    for line in lines:
        values = []
        numbers = line.split(' ')
        for n in numbers:
            values.append(int(n))

        safe = 0
        for index, e in enumerate(values):
            values_copy = values.copy()
            values_copy.pop(index)
            decreasing = all((i > j and i - j <= 3) for i, j in zip(values_copy, values_copy[1:]))
            increasing = all((i < j and j - i <= 3) for i, j in zip(values_copy, values_copy[1:]))
            if (decreasing or increasing):
                safe = 1

        safe_list.append(safe)

    print(sum(safe_list))

if __name__ == '__main__':
    part1()
    part2()
