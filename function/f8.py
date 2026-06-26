# return value with  no argument
def check():
	print("enter a number")
	no=int(input())
	if no%2==0:
		return "even"
	else:
		return "odd"
res=check()		
print(res)
	
		
	