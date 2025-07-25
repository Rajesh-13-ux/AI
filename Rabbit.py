from collections import deque

class State:
    def __init__(self, val, path=None):
        self.val = val
        self.path = path or [val]

    def is_goal(self):
        return self.val == "EEE_WWW"

    def next(self):
        res = []
        a = list(self.val)
        i = self.val.index('_')

        if i < 6 and a[i + 1] == 'E':
            b = a[:]
            b[i], b[i + 1] = b[i + 1], b[i]
            res.append(State("".join(b), self.path + ["".join(b)]))

        if i < 5 and a[i + 2] == 'E' and a[i + 1] == 'W':
            b = a[:]
            b[i], b[i + 2] = b[i + 2], b[i]
            res.append(State("".join(b), self.path + ["".join(b)]))

        if i > 0 and a[i - 1] == 'W':
            b = a[:]
            b[i], b[i - 1] = b[i - 1], b[i]
            res.append(State("".join(b), self.path + ["".join(b)]))

        if i > 1 and a[i - 2] == 'W' and a[i - 1] == 'E':
            b = a[:]
            b[i], b[i - 2] = b[i - 2], b[i]
            res.append(State("".join(b), self.path + ["".join(b)]))

        return res

def bfs(start):
    seen = set()
    q = deque([State(start)])
    while q:
        s = q.popleft()
        if s.is_goal():
            return s.path
        for nxt in s.next():
            if nxt.val not in seen:
                seen.add(nxt.val)
                q.append(nxt)
    return []

def dfs(start):
    seen = set()
    stk = [State(start)]
    while stk:
        s = stk.pop()
        if s.is_goal():
            return s.path
        for nxt in s.next():
            if nxt.val not in seen:
                seen.add(nxt.val)
                stk.append(nxt)
    return []

start = "WWW_EEE"

print("BFS Path:")
for step in bfs(start):
    print(step)

print("\nDFS Path:")
for step in dfs(start):
    print(step)
