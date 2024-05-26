def determinant(xp,yp, xq,yq, xr,yr):
    det = 1*xq*yr + 1*xr*yp + 1*xp*yq - 1*xq*yp - 1*xr*yq - 1*xp*yr
    return det

n = int(input())
P = []
answer = []
left = 0
right = 0
neutral = 0
for i in range(n):
    xi, yi = map(int, input().split())
    if (i==0):
        x1, y1 = xi, yi
    P.append((xi, yi))

P.append((x1, y1))

for i in range(n):
    if (i==n-1):
        break
    xp, yp = P[i]
    xq, yq = P[i+1]
    xr, yr = P[i+2]
    if (determinant(xp,yp, xq,yq, xr,yr) > 0):
        left += 1
    elif (determinant(xp,yp, xq,yq, xr,yr) < 0):
        right += 1
    else:
        neutral += 1


print(left, right, neutral)