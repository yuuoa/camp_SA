import time

rangee = []
for j in range(1,1000000,1):
	rangee.append(j)
print ("number of index= ", rangee.index(j)+1)
while True:
	a=int(input('enter number to be search: '))
	if a<10000001 and a>0:
		break
start = time.time()

def binary(x, item):
	y = 0
	z = len(x)-1
	found = False
	
	while y<=z and not found:
		midpoint = (y + z)//2
		if x[midpoint]==item:
			found = True
		else:
			if item<x[midpoint]:
				z=midpoint-1
			else:
				y = midpoint+1
	return found

length=len(rangee)

print()
print("number found on index",rangee.index(a))
end = time.time()
print ('execution time: ',(end-start),'s')
