def flash(mx, i, j):
    mx[i][j] = 0
    for k in range(i - 1, i + 2):
        for l in range(j - 1, j + 2):
            if (k, l) != (i, j) and 0 <= k < len(mx) and 0 <= l < len(mx[0]):
                mx[k][l] += 1 * mx[k][l] != 0
                if mx[k][l] > 9: 
                    mx = flash(mx, k, l)
    return mx

def apply_step(mx):
    for i in range(len(mx)):
        mx[i] = [x + 1 for x in mx[i]]
    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if mx[i][j] > 9:
                mx = flash(mx, i, j)
    return sum(x.count(0) for x in mx)

def is_sync_step(mx, test_row):
    for i in range(len(mx)):
        if mx[i] != test_row:
            return False
    return True

with open('11\\11.in', 'r') as f:
    mx = [[int(x) for x in line.strip()] for line in f.readlines()]
num_steps = 100
test_row = [0 for _ in range(len(mx[0]))]
i, part1, part2, sync_found = 0, 0, -1, False
while (True):
    if (sync_found and i >= num_steps):
        break
    temp = apply_step(mx)
    part1 += temp * (i < num_steps)
    if is_sync_step(mx, test_row):
        sync_found, part2 = True, i
    i += 1
print(f"{part1}\n{part2 + 1}")