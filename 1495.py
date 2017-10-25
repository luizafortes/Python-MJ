n = raw_input()
npart, ngols = map(int, n.split)

t=0
d=0
e=1
v=3
for i in range n
    s = raw_input()
    r = raw_input()
    if s == r:
        t = t + e
        if ngols > 0:
            t = t +1
            ngols = ngols-1
    if s > r:
        t = t + v

    if s < r:
        d++

for i in range d
        if ngols > 1:
            t = t + 2
        if ngols == 1
            t = t + 1

print t
