from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.counter = 0

	def add(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def all_paths_util(self, u, d, v):
		if u.islower(): v[u] += 1
		if u == d: self.counter += 1
		else:
			for i in self.graph[u]:
				if ((i not in v.keys() or v[i]== 0) or 
					(i not in ['start'] and v[i] == 1 and 2 not in v.values())): #remove line for part 1
					self.all_paths_util(i, d, v)
		if u.islower():
			v[u] -= 1

	def all_paths(self, s, d):
		v ={x : 0 for x in self.graph.keys() if x.islower()}
		for key in self.graph.keys(): self.graph[key].sort()
		self.all_paths_util(s, d, v)

with open('12\\12.in', 'r') as f:
	l = [line.strip().split('-') for line in f.readlines()]
g = Graph()
for line in l: g.add(line[0], line[1])
g.all_paths('start', 'end')
print(g.counter)