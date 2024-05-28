from itertools import combinations

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"{self.a}x + {self.b}y = {self.c}"

def find_interesting_rectangle(equations):
    min_x, max_x = float('-inf'), float('inf')
    min_y, max_y = float('-inf'), float('inf')

    for eq in equations:
        if eq.a != 0 and eq.b == 0:
            x_value = -eq.c / eq.a
            if eq.a > 0:
                max_x = min(max_x, x_value)
            else:
                min_x = max(min_x, x_value)
        elif eq.a == 0 and eq.b != 0:
            y_value = -eq.c / eq.b
            if eq.b > 0:
                max_y = min(max_y, y_value)
            else:
                min_y = max(min_y, y_value)

    if min_x > max_x or min_y > max_y:
        return None
    if min_x == float('-inf') or max_x == float('inf') or min_y == float('-inf') or max_y == float('inf'):
        return None
    return (min_x, max_x, min_y, max_y)

def is_point_inside_rectangle(point, rect):
    min_x, max_x, min_y, max_y = rect
    return min_x < point.x < max_x and min_y < point.y < max_y

def process_points(equations, points):
    min_area = float('inf')
    best_rect = None

    for r in range(1, len(equations) + 1):
        for subset in combinations(equations, r):
            rect = find_interesting_rectangle(subset)
            if rect is not None:
                area = (rect[1] - rect[0]) * (rect[3] - rect[2])
                if area < min_area:
                    min_area = area
                    best_rect = rect

    if best_rect is None:
        for point in points:
            print("NO")
        return

    for point in points:
        if is_point_inside_rectangle(point, best_rect):
            print("YES")
            print(f"{min_area:.6f}")
        else:
            print("NO")

n = int(input())
equations = []

for i in range(n):
    ai, bi, ci = map(int, input().split())
    equations.append(Equation(ai, bi, ci))

m = int(input())
points = []

for i in range(m):
    xi, yi = map(float, input().split())
    points.append(Point(xi, yi))

process_points(equations, points)
