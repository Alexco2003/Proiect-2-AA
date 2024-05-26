# Graham’s scan, varianta Andrew (algoritm)

def determinant(xp,yp, xq,yq, xr,yr):
    det = 1*xq*yr + 1*xr*yp + 1*xp*yq - 1*xq*yp - 1*xr*yq - 1*xp*yr
    return det

def distantaLaPatrat(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2

n = int(input())
P = []
k = 0
for i in range(n):
    xi, yi = map(int, input().split())
    P.append((xi, yi))

P.sort()

Li = []
Li.append(P[0])
Li.append(P[1])

for i in range(2, n):
    Li.append(P[i])
    while len(Li) > 2 and determinant(Li[-3][0], Li[-3][1], Li[-2][0], Li[-2][1], Li[-1][0], Li[-1][1]) <= 0:
        Li.pop(-2)


Ls = []
Ls.append(P[-1])
Ls.append(P[-2])

for i in range(n-3, -1, -1):
    Ls.append(P[i])
    while len(Ls) > 2 and determinant(Ls[-3][0], Ls[-3][1], Ls[-2][0], Ls[-2][1], Ls[-1][0], Ls[-1][1]) <= 0:
        Ls.pop(-2)

L = Li + Ls[1:-1]

print(len(L))
for Pi in L:
    print(Pi[0], Pi[1])






