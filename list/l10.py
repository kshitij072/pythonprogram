#count no of even and odd in list
L=[5,9,8,7,5,6]
ev=0
od=0
for i in L:
	if i%2==0:
		ev=ev+1
	else:
		od=od+1
print("even=",ev)
print("odd=",od)		