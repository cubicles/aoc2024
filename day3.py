import re

def part1():
    with open('input3.txt') as file:
        lines = [line.rstrip() for line in file]
        big_line = ''.join(lines)

    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, big_line)

    products = []
    for pair in matches:
        a = int(pair.split('mul(')[1].split(',')[0])
        b = int(pair.split(',')[1].split(')')[0])
        products.append(a * b)

    print(sum(products))

def part2():
    with open('input3.txt') as file:
        lines = [line.rstrip() for line in file]
        big_line = ''.join(lines)

    # pattern = r"\b(?:mul\(\d+,\d+\)|don't\(\)|do\(\))\b"
    pattern = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    matches = re.findall(pattern, big_line)

    products = []
    status = True
    for pair in matches:
        if pair == "do()":
            status = True
        elif pair == "don't()":
            status = False
        else:
            if status:
                a = int(pair.split('mul(')[1].split(',')[0])
                b = int(pair.split(',')[1].split(')')[0])
                products.append(a * b)

    print(sum(products))

if __name__ == '__main__':
    part1()
    part2()
