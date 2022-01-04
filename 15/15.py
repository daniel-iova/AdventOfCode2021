from collections import namedtuple
import heapq as hq

Cell = namedtuple('Cell', 'dist x y')

def is_inside(n, i, j):
    return (0 <= i < n and 0 <= j < n)

MAX = 2307895232359

def solve(m):
    dist = []
    for _ in range(len(m)):
        dist.append([MAX] * len(m))

    moves = [(0,1), (0, -1), (1, 0), (-1, 0)]

    st = [Cell(0, 0, 0)]
    hq.heapify(st)

    dist[0][0] = m[0][0]

    while len(st) > 0:
        k = hq.heappop(st)
        for move in moves:
            new_x = k.x + move[0]
            new_y = k.y + move[1]
            if not is_inside(len(m), new_x, new_y):
                continue

            if dist[new_x][new_y] > dist[k.x][k.y] + m[new_x][new_y]:
                if dist[new_x][new_y] != MAX:
                    st.remove(Cell(dist[new_x][new_y], new_x, new_y))
                
                dist[new_x][new_y] = dist[k.x][k.y] + m[new_x][new_y]
                hq.heappush(st, Cell(dist[new_x][new_y], new_x, new_y))
    return dist[len(m) - 1][len(m) - 1]
            

def get_full_map(m: list[list[int]]):
    fm = []
    for i in range(len(m) * 5):
        fm.append([0] * len(m) * 5)

    for i in range(len(fm)):
        for j in range(len(fm)):
            fm[i][j] = m[i % len(m)][j % len(m)]
            if i >= len(m):
                fm[i][j] += int(i / len(m))
            if j >= len(m):
                fm[i][j] += int(j / len(m))
            if fm[i][j] > 9:
                fm[i][j] = fm[i][j] - 9
    return fm 


m = []
with open("15\\15.in", 'r') as f:
    for line in f:
        m.append([int(x) for x in line.strip()])

print(solve(m) - m[0][0])

fm = get_full_map(m)

print(solve(fm) - fm[0][0])