def part1():
    with open('input1.txt') as file:
        lines = [line.rstrip() for line in file]
    left = []
    right = []
    for line in lines:
        left.append(line.split('   ')[0])
        right.append(line.split('   ')[1])

    left.sort()
    right.sort()

    distance = []
    for count, _ in enumerate(left):
        distance.append(abs(int(left[count]) - int(right[count])))
    print(sum(distance))
    return left, right

def part2(left, right):
    similarities = []
    for item in left:
        c = 0
        for r in right:
            if (item == r):
                c = c + 1
        similarities.append(int(item) * c)
    print(sum(similarities))

if __name__ == '__main__':
    left, right = part1()
    part2(left, right)
