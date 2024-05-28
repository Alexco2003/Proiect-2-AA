class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Operation:
    def __init__(self, op_type, y, a, b):
        self.type = op_type
        self.y = y
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.y < other.y

maxX = 1000005
SIZE = 2 * maxX

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx

    def query(self, idx):
        sum = 0
        while idx > 0:
            sum += self.tree[idx]
            idx -= idx & -idx
        return sum

n = int(input())
segments = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((Point(x1, y1), Point(x2, y2)))

horizontal_segments = []
vertical_segments = []
ops = []

for s in segments:
    if s[0].x == s[1].x:
        vertical_segments.append(s)
        ops.append(Operation(2, s[0].y, s[0].x + maxX, -1))
        ops.append(Operation(3, s[1].y, s[0].x + maxX, -1))
    else:
        horizontal_segments.append(s)
        ops.append(Operation(1, s[0].y, s[0].x + maxX, s[1].x + maxX))

ops.sort()

fenwick_tree = FenwickTree(SIZE)
cnt = 0

for op in ops:
    if op.type == 1:
        cnt += fenwick_tree.query(op.b) - fenwick_tree.query(op.a - 1)
    elif op.type == 2:
        fenwick_tree.update(op.a, 1)
    elif op.type == 3:
        fenwick_tree.update(op.a, -1)

print(cnt)
