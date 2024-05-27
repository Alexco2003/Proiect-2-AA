class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def determinant4(A,B,C,D):
    det = (-1)**5 * (((B.x-A.x)*(C.y-A.y)*(D.x**2+D.y**2-A.x**2-A.y**2)) + ((C.x-A.x)*(D.y-A.y)*(B.x**2+B.y**2-A.x**2-A.y**2)) + ((D.x-A.x)*(B.y-A.y)*(C.x**2+C.y**2-A.x**2-A.y**2)) - ((C.x-A.x)*(B.y-A.y)*(D.x**2+D.y**2-A.x**2-A.y**2)) - ((B.x-A.x)*(D.y-A.y)*(C.x**2+C.y**2-A.x**2-A.y**2)) - ((D.x-A.x)*(C.y-A.y)*(B.x**2+B.y**2-A.x**2-A.y**2)))
    return det

xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

A = Point(xA, yA)
B = Point(xB, yB)
C = Point(xC, yC)

m=int(input())

P=[]
for i in range(m):
    xi, yi = map(int, input().split())
    P.append(Point(xi, yi))

for i in range(m):
    if determinant4(A,B,C,P[i]) == 0:
        print("BOUNDARY")
    elif determinant4(A,B,C,P[i]) > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")
