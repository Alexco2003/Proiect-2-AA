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

def find_interesting_rectangle(equations, point):
    min_x, max_x = float('-inf'), float('inf')
    min_y, max_y = float('-inf'), float('inf')

    for eq in equations:
        if eq.a != 0 and eq.b == 0:
            x_value = -eq.c / eq.a
            if eq.a > 0:
                if point.x < x_value:
                    max_x = min(max_x, x_value)
            else:
                if point.x > x_value:
                    min_x = max(min_x, x_value)
        elif eq.a == 0 and eq.b != 0:
            y_value = -eq.c / eq.b
            if eq.b > 0:
                if point.y < y_value:
                    max_y = min(max_y, y_value)
            else:
                if point.y > y_value:
                    min_y = max(min_y, y_value)

    if min_x >= max_x or min_y >= max_y:
        return None
    return (min_x, max_x, min_y, max_y)

def is_point_inside_rectangle(point, rect):
    min_x, max_x, min_y, max_y = rect
    return min_x < point.x < max_x and min_y < point.y < max_y

def process_points(equations, points):
    results = []

    for point in points:
        min_area = float('inf')
        found = False

        for r in range(1, len(equations) + 1):
            for subset in combinations(equations, r):
                rect = find_interesting_rectangle(subset, point)
                if rect is not None and is_point_inside_rectangle(point, rect):
                    area = (rect[1] - rect[0]) * (rect[3] - rect[2])
                    if area < min_area:
                        min_area = area
                        found = True

        if found:
            results.append((True, min_area))
        else:
            results.append((False, None))

    for result in results:
        if result[0]:
            print("YES")
            print(f"{result[1]:.6f}")
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
