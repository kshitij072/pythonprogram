#check no divisible by only5 only7 both5,7  none
print("enter a number")
no=int(input())
if no%35==0:
	print("both")
elif  no%5==0:
	print("onlyfive")
elif  no%7==0:
	print("onlyseven")
else:
	print("none")