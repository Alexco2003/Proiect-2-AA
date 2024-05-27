# Jarvis’ march / Jarvis’ wrap [1973]

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

A1 = min(P)
k=1
valid = True
answer = []
answer.append(A1)
S = A1
while valid:
    for Pi in P:
        if (Pi != answer[k-1]):
            S=Pi
            break
    for i in range(n):
        xp, yp = answer[k-1]
        xq, yq = S
        xr, yr = P[i]
        det = determinant(xp,yp, xq,yq, xr,yr)
        if det < 0 or (det == 0 and distantaLaPatrat(xp, yp, xr, yr) > distantaLaPatrat(xp, yp, xq, yq)):
            S = P[i]
    if S!=A1:
        k=k+1
        answer.append(S)
    else:
        valid = False

print(k)
for Pi in answer:
    print(Pi[0], Pi[1])







