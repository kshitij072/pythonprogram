def sdtest():
	print("enter the number")
	no=int(input())
	s=0
	while no!=0:
		r=no%10
		s=s+r
		no=no//10
	print("sum of digits=",s)
sdtest()