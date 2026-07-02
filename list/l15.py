#show biggest element
L=[5,9,8,17,11,5,6]
big=L[0]
for i in range(1,len(L),1):
	if big<L[i]:
		big=L[i]
print(big)		