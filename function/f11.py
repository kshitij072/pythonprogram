 #return value with  argument
def check(no):
 	if no%2==0:
 		return "even"
 	else:
 		return "odd"
print("enter a number")
no=int(input())
res=check(no)
print(res)		