#no return value with  argument
def check(no):
	if no%2==0:
		print("is even number")
	else:
		print("is odd number")
print("enter a number")
no=int(input())
check(no)		