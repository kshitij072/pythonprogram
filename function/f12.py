# return value with  argument
def sical(p,r,t):
	s=(p*r*t)/100
	return s
print("enter principal")
p=int(input())
print("enter rate")
r=int(input())
print("enter time")
t=int(input())
res=sical(p,r,t)
print("simple interest=",res)	
