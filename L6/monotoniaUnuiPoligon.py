class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def is_monotone(points, axis):
    if axis == 'x':
        min_x = min(points, key=lambda point: point.x)
        max_x = max(points, key=lambda point: point.x)
        min_idx = points.index(min_x)
        max_idx = points.index(max_x)

        points = points[min_idx:] + points[:min_idx]

        for i in range(1, len(points)):
            if points[i-1].x > points[i].x:
                return "NO"
            if points[i] == max_x:
                break

        points = points[min_idx:] + points[:min_idx]

        for i in range(len(points)-1, max_idx, -1):
            if points[i].x > points[i-1].x:
                return "NO"

        return "YES"

    elif axis == 'y':
        min_y = min(points, key=lambda point: point.y)
        max_y = max(points, key=lambda point: point.y)
        min_idx = points.index(min_y)
        max_idx = points.index(max_y)

        points = points[min_idx:] + points[:min_idx]

        for i in range(1, len(points)):
            if points[i-1].y > points[i].y:
                return "NO"
            if points[i] == max_y:
                break

        points = points[min_idx:] + points[:min_idx]

        for i in range(len(points)-1, max_idx, -1):
            if points[i].y > points[i-1].y:
                return "NO"

        return "YES"

n = int(input())
P = []
for i in range(n):
    xi, yi = map(int, input().split())
    P.append(Point(xi, yi))

print(is_monotone(P.copy(), 'x'))
print(is_monotone(P.copy(), 'y'))
