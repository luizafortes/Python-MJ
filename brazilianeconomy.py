q = raw_input()
vi = raw_input()
vi = map (int, vi.split())
y=0
n=0

for i in range(int(q)):
	if vi[i]==0:
		y=y+1
	if vi[i]==1:
		n=n+1

if y>n:
	print("Y")
if n>=y:
	print("N")
