print("enter the number")
no=int(input())
ec=0
oc=0
while no!=0:
	r=no%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	no=no//10	
print("number of even digits=",ec)

print("number of odd digits=",oc)