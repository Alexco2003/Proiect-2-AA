class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def determinant(xp, yp, xq, yq, xr, yr):
    return xq * yr + xr * yp + xp * yq - xq * yp - xr * yq - xp * yr

def point_on_segment(a, b, p):
    if determinant(a.x, a.y, b.x, b.y, p.x, p.y) == 0:
        return min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y)
    return False

def do_intersect(p1, q1, p2, q2):
    d1 = determinant(p1.x, p1.y, q1.x, q1.y, p2.x, p2.y)
    d2 = determinant(p1.x, p1.y, q1.x, q1.y, q2.x, q2.y)
    d3 = determinant(p2.x, p2.y, q2.x, q2.y, p1.x, p1.y)
    d4 = determinant(p2.x, p2.y, q2.x, q2.y, q1.x, q1.y)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True

    if d1 == 0 and point_on_segment(p1, q1, p2):
        return True

    if d2 == 0 and point_on_segment(p1, q1, q2):
        return True

    if d3 == 0 and point_on_segment(p2, q2, p1):
        return True

    if d4 == 0 and point_on_segment(p2, q2, q1):
        return True

    return False

def is_inside_polygon(polygon, p):
    max_x = max(polygon, key=lambda x: x.x).x
    max_y = max(polygon, key=lambda x: x.y).y
    M = Point(max_x + 256, max_y + 256)

    count = i = 0
    n = len(polygon)

    while True:
        next = (i + 1) % n
        if do_intersect(polygon[i], polygon[next], p, M):
            if determinant(polygon[i].x, polygon[i].y, p.x, p.y, polygon[next].x, polygon[next].y) == 0:
                return "BOUNDARY" if point_on_segment(polygon[i], polygon[next], p) else "OUTSIDE"
            count += 1
        i = next
        if i == 0:
            break

    return "INSIDE" if count % 2 == 1 else "OUTSIDE"

n = int(input())
P = []
for i in range(n):
    xi, yi = map(int, input().split())
    P.append(Point(xi, yi))

m = int(input())
Q = []
for i in range(m):
    xi, yi = map(int, input().split())
    Q.append(Point(xi, yi))

for point in Q:
    print(is_inside_polygon(P, point))
