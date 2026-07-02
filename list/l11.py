#add odd and even digits
L=[5,9,8,7,5,6]
os=0
es=0
for i in L:
	if i%2==0:
		es=es+i
	else:
		os=os+i
print("sum of even=",es)
print("sum of odd=",os)		