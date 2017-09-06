def twd(i,j):


    v=1
    t=0

    x=j-1
    while x >= 0:
        if m[i][j] <= m[i][x]:
            v=0
            break
        x-=1
    t+=v

    v=1

    x=j+1
    while x < c:
        if m[i][j] <= m[i][x]:
            v=0
            break
        x+=1
    t+=v

    v=1

    y=i-1
    while y >= 0:
        if m[i][j] <= m[y][j]:
            v=0
            break
        y-=1
    t+=v

    v=1
    y=i+1
    while y < r:
        if m[i][j] <= m[y][j]:
            v=0
            break
        y+=1
    t+=v

    return t

r,c = map(int,raw_input().split())
m=[]

for i in range(r):
    s = raw_input()
    m.append(map(int,s.split()))
w=0
for i in range(r):
    for j in range(c):
        w+=twd(i,j)

print w
