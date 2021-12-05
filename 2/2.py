horizontal, depth, aim = 0, 0, 0

with (open("2\\2.in", "r") as f):
    for l in f:
        num = int(l.split()[1])
        if (l[0] == 'f'):
            horizontal += num
            depth += aim * num
        elif (l[0] == 'u'):
            aim -= num
        elif (l[0] == 'd'):
            aim += num

print (horizontal*depth)
