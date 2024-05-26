def determinant(xp,yp, xq,yq, xr,yr):
    det = 1*xq*yr + 1*xr*yp + 1*xp*yq - 1*xq*yp - 1*xr*yq - 1*xp*yr
    return det

t = int(input())
answer = []
for i in range(t):
    xp,yp, xq,yq, xr,yr = map(int, input().split())
    if (determinant(xp,yp, xq,yq, xr,yr) > 0):
        answer.append("LEFT")
    elif (determinant(xp,yp, xq,yq, xr,yr) < 0):
        answer.append("RIGHT")
    else:
        answer.append("TOUCH")

for i in answer:
    print(i)