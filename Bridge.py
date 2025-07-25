from collections import deque

names = ['Amogh', 'Ameya', 'Grandma', 'Grandpa']
times = [5, 10, 20, 25]

class State:
    def __init__(self, pos, side, cost, prev, move):
        self.pos = pos
        self.side = side
        self.cost = cost
        self.prev = prev
        self.move = move  # (who moved, time taken, direction)

    def is_goal(self):
        return self.pos == [1, 1, 1, 1] and self.side == 1 and self.cost <= 60

    def next(self):
        res = []
        idx = [i for i in range(4) if self.pos[i] == self.side]
        if self.side == 0:
            for i in range(len(idx)):
                for j in range(i, len(idx)):
                    a, b = idx[i], idx[j]
                    new_pos = self.pos[:]
                    new_pos[a] = 1
                    new_pos[b] = 1
                    t = max(times[a], times[b])
                    people = (a, b)
                    move = ([names[a], names[b]], t, "→")
                    res.append(State(new_pos, 1, self.cost + t, self, move))
        else:
            for i in idx:
                new_pos = self.pos[:]
                new_pos[i] = 0
                t = times[i]
                move = ([names[i]], t, "←")
                res.append(State(new_pos, 0, self.cost + t, self, move))
        return res

def reconstruct_path(s):
    path = []
    while s:
        path.append(s)
        s = s.prev
    return path[::-1]

def print_path(path):
    for s in path:
        if s.move:
            who, t, dir = s.move
            print(f"{' and '.join(who)} {dir} ({t} min) → Total: {s.cost} min")

def bfs():
    start = State([0, 0, 0, 0], 0, 0, None, None)
    q = deque([start])
    seen = set()
    while q:
        s = q.popleft()
        key = (tuple(s.pos), s.side)
        if key in seen or s.cost > 60:
            continue
        seen.add(key)
        if s.is_goal():
            return reconstruct_path(s)
        for nxt in s.next():
            q.append(nxt)
    return []

def dfs():
    start = State([0, 0, 0, 0], 0, 0, None, None)
    stk = [start]
    seen = set()
    while stk:
        s = stk.pop()
        key = (tuple(s.pos), s.side)
        if key in seen or s.cost > 60:
            continue
        seen.add(key)
        if s.is_goal():
            return reconstruct_path(s)
        for nxt in reversed(s.next()):
            stk.append(nxt)
    return []

print("=== BFS Path ===")
bfs_path = bfs()
print_path(bfs_path)

print("\n=== DFS Path ===")
dfs_path = dfs()
print_path(dfs_path)
