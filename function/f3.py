#no return value with no argument
def sical():
	print("enter principal")
	p=int(input())
	print("enter rate")
	r=int(input())
	print("enter time")
	t=int(input())
	s=(p*r*t)/100
	print("sical=",s)
	return
sical()	