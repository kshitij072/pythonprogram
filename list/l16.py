#show smallest element
L=[5,9,8,17,11,5,6]
small=L[0]
for i in range(1,len(L),1):
	if small>L[i]:
		small=L[i]
print(small)	
