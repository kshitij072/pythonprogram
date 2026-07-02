#segregate odd and even numbers and make odd list,even list
L=[5,9,8,7,5,6]
oL=[]
eL=[]
for i in L:
	if i%2==0:
		oL.append(i)
	else:
		eL.append(i)
print(oL)
print(eL)		
	