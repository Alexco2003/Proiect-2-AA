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

def process_points(equations, points):
    horizontal_equations = [eq for eq in equations if eq.b != 0]
    vertical_equations = [eq for eq in equations if eq.a != 0]

    for point in points:
        min_x, max_x = float('-inf'), float('inf')
        min_y, max_y = float('-inf'), float('inf')

        for eq in horizontal_equations:
            y_value = -eq.c / eq.b
            if eq.b > 0:
                if point.y < y_value:
                    max_y = min(max_y, y_value)
            else:
                if point.y > y_value:
                    min_y = max(min_y, y_value)

        for eq in vertical_equations:
            x_value = -eq.c / eq.a
            if eq.a > 0:
                if point.x < x_value:
                    max_x = min(max_x, x_value)
            else:
                if point.x > x_value:
                    min_x = max(min_x, x_value)

        if min_x >= max_x or min_y >= max_y or \
           min_x == float('-inf') or max_x == float('inf') or \
           min_y == float('-inf') or max_y == float('inf'):
            print("NO")
        else:
            area = (max_x - min_x) * (max_y - min_y)
            print("YES")
            print(f"{area:.6f}")

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
