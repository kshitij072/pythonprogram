a=10
def show():
	global a
	a=20

	print("global ",a)
	
def disp():
	b=30
	print(b)
	print(a)

show()
disp()	