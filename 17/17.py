def in_range(x, y, x0, y0):
    sx = sy = 0
    m = 34976389467348
    while True:
        sx += x0
        sy -= y0
        if x0 > 0:
            x0 -= 1
        elif x0 < 0:
            x0 += 1
        y0 -= 1
        m = min(m, sy)
        if x[0] <= sx <= x[1] and y[1] <= sy <= y[0]:
            return True, m
        if sx > x[1] or sy > y[0]:
            return False, 0

def get_start_val(x):
    i = 0
    while True:
        if x[0] <= i*(i + 1)/2 <= x[1]:
            return i
        i += 1

with open('17\\17.in', 'r') as f:
    x,y = [tuple(abs(int(j)) for j in i.strip()[2:].split('..')) for i in f.readline().strip()[13:].split(',')]

m = 34976389467348
vals = 0
for i in range(get_start_val(x), x[1] + 1):
    for j in range(-y[0], y[0] + 1):
        b, v = in_range(x, y, i, j)
        if b:
            vals += 1
            m = min(m, v)

print(abs(m), vals)