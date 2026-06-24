#find largest among three numbers using if else
print("enter number A")
A=float(input())
print("enter number B")
B=float(input())
print("enter number C")
C=float(input())
if A>B and A>C:
	print("A is the largest number")
elif B>A and B>C:
	print("B is the largest number")
elif C>A and C>B:
	print("C is the largest number")
