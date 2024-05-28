class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

n = int(input())
segments = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    segments.append((Point(x1, y1), Point(x2, y2)))

horizontal_segments = []
vertical_segments = []

for s in segments:
    if s[0].x == s[1].x:
        vertical_segments.append(s)
    else:
        horizontal_segments.append(s)

cnt = 0

for h in horizontal_segments:
    for v in vertical_segments:
        if min(h[0].x, h[1].x) <= v[0].x <= max(h[0].x, h[1].x) and \
           min(v[0].y, v[1].y) <= h[0].y <= max(v[0].y, v[1].y):
            cnt += 1

print(cnt)
