n = 12

def part1():
    ls = [[0, 0] for _ in range(n)]
    gamma_rate = 0
    epsilon_rate = 0
    with (open("3\\3.in", "r") as f):
        for line in f:
            for i in range(n):
                ls[i][int(line[i])] += 1
        for i in range(n - 1, -1, -1):
            bit = 1 if ls[i][1] >= ls[i][0] else 0
            gamma_rate += bit * 2**(n - i - 1)
            epsilon_rate += (1 - bit) * 2**(n - i - 1)
    print(gamma_rate * epsilon_rate)

def build_str(lines, added_bit):
    out_str = ''
    ls = [[0, 0] for _ in range(n)]
    for i in range(n):
        x = [line.strip() for line in lines if line[:i] == out_str]
        if (len(x) == 1):
            out_str = x[0]
            break
        for line in x:
            ls[i][int(line[i])] += 1
        out_str += str(added_bit) if ls[i][1] >= ls[i][0] else str(1 - added_bit)  
    return int(out_str, 2)

def part2():
    with (open("3\\3.in", "r") as f):
        lines = f.readlines()
        print (build_str(lines, 1) * build_str(lines, 0))            


part1()     
part2()