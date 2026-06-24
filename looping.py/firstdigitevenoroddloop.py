print("enter the numnber")
n=int(input())
while n!=0:
	r=n%10
	n=n//10
	
print(r)	

if r%2==0:

	print("even")
else:
	print("odd")	