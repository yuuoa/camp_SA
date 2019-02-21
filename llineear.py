import time

rangee = []
for j in range(1,1000000000,1):
	rangee.append(j)
print ("number of index= ", rangee.index(j)+1)
#print(rangee)
while True:
	a=int(input("enter number to be search: "))
	if a<1000000001 and a>0:
		break
start = time.time()

def linearS(a, item):
	j = 0
	y = 0
	z = len(a)-1
	found = False	
	while j<=z and not found:
		y+=1
		if a[y]==item:
			found = True
		else: j = j+1
		
list_length=len(rangee)

print()
print("number found on index: ",rangee.index(a))
end = time.time()
print ("execution time= ",(end-start),"s")
