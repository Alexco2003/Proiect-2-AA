class Equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"{self.a}x + {self.b}y = {self.c}"


def intersection(equations):
    x_min, x_max = -float('inf'), float('inf')
    y_min, y_max = -float('inf'), float('inf')

    for eq in equations:
        if eq.a != 0 and eq.b == 0:
            x_value = -eq.c / eq.a
            if eq.a > 0:
                x_max = min(x_max, x_value)
            else:
                x_min = max(x_min, x_value)
        elif eq.a == 0 and eq.b != 0:
            y_value = -eq.c / eq.b
            if eq.b > 0:
                y_max = min(y_max, y_value)
            else:
                y_min = max(y_min, y_value)

    if x_min > x_max or y_min > y_max:
        return "VOID"
    elif x_min == -float('inf') or x_max == float('inf') or y_min == -float('inf') or y_max == float('inf'):
        return "UNBOUNDED"
    else:
        return "BOUNDED"

n = int(input())
P = []
for i in range(n):
    ai, bi, ci = map(int, input().split())
    P.append(Equation(ai, bi, ci))

result = intersection(P)
print(result)
