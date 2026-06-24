print("enter x coordinate")
x=float(input())
print("enter y coordinate")
y=float(input())
if x==0 and y==0:
	print("point lies at the origin")
elif x==0:
	print("point lies in y axis")
elif y==0:
	print("point lies in x axis")
elif x>0 and y>0:
	print("point lies in first quadrant")
elif x<0 and y>0:
	print("point lies in second quadrant")
elif x<0 and y<0:
	print("point lies in third quadrant")
else:
	print("point lies in 4th quadrant")