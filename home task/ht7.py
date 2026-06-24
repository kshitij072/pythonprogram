#Write a python Program that prompts the user to enter an integer and determines whether it is divisible by 5 and 6, whether it is divisible by 5 or 6, and whether it is divisible by 5 or 6, but not both
print("enter a number")
no=int(input())
if no%30==0:
	print("divisible by both")
elif no%6==0:
	print("divisible by 6")
elif no%5==0:
	print("divisible by 5")
else:
	print("not divisible")