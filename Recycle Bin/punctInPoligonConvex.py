def determinant(xp,yp, xq,yq, xr,yr):
    det = 1*xq*yr + 1*xr*yp + 1*xp*yq - 1*xq*yp - 1*xr*yq - 1*xp*yr
    return det

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def cross_product(self, a, b):
        return (a - self).cross(b - self)

    def dot_product(self, a, b):
        return (a - self).dot(b - self)

    def sqr_len(self):
        return self.dot(self)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def lex_comp(p1, p2):
    return (p1.x < p2.x) or (p1.x == p2.x and p1.y < p2.y)

def sgn(val):
    return 1 if val > 0 else (0 if val == 0 else -1)

def point_in_triangle(a, b, c, p):
    s1 = abs(a.cross_product(b, c))
    s2 = abs(p.cross_product(a, b)) + abs(p.cross_product(b, c)) + abs(p.cross_product(c, a))
    return s1 == s2

def point_on_segment(a, b, p):
    if determinant(a.x, a.y, b.x, b.y, p.x, p.y) == 0:
        return min(a.x, b.x) <= p.x <= max(a.x, b.x) and min(a.y, b.y) <= p.y <= max(a.y, b.y)
    return False

def prepare(points):
    global seq, translation, n
    n = len(points)
    pos = 0
    for i in range(1, n):
        if lex_comp(points[i], points[pos]):
            pos = i

    points = points[pos:] + points[:pos]

    n -= 1
    seq = [points[i + 1] - points[0] for i in range(n)]
    translation = points[0]

def point_in_convex_polygon(point):
    global seq, translation, n
    point = point - translation

    if point_on_segment(Point(0, 0), seq[0], point):
        return "BOUNDARY"
    if point_on_segment(seq[n - 1], Point(0, 0), point):
        return "BOUNDARY"


    if sgn(determinant(0, 0, seq[0].x, seq[0].y, point.x, point.y)) != sgn(determinant(0, 0, seq[0].x, seq[0].y, seq[n - 1].x, seq[n - 1].y)) or \
       sgn(determinant(0, 0, seq[n - 1].x, seq[n - 1].y, point.x, point.y)) != sgn(determinant(0, 0, seq[n - 1].x, seq[n - 1].y, seq[0].x, seq[0].y)):
        return "OUTSIDE"

    if determinant(0, 0, seq[0].x, seq[0].y, point.x, point.y) == 0:
        return "BOUNDARY" if seq[0].sqr_len() >= point.sqr_len() else "OUTSIDE"

    l, r = 0, n - 1
    while r - l > 1:
        mid = (l + r) // 2
        if determinant(0, 0, seq[mid].x, seq[mid].y, point.x, point.y) >= 0:
            l = mid
        else:
            r = mid

    if point_on_segment(seq[l], seq[l + 1], point):
        return "BOUNDARY"

    return "INSIDE" if point_in_triangle(seq[l], seq[l + 1], Point(0, 0), point) else "OUTSIDE"

n = int(input())
P = []
for i in range(n):
    xi, yi = map(int, input().split())
    P.append(Point(xi, yi))

m = int(input())
R = []
for i in range(m):
    xi, yi = map(int, input().split())
    R.append(Point(xi, yi))

prepare(P)

for r in R:
    print(point_in_convex_polygon(r))

# wrong pe testul 4 dar 9/10