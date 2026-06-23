#Write a Java program that reads three integers from the user and prints "Increasing" if the numbers are in increasing order, "Decreasing" if the numbers are in decreasing order, and "Neither increasing nor decreasing order" otherwise
print("enter first number A")
A=int(input())
print("enter second number B")
B=int(input())
print("enter third number C")
C=int(input())
if A<B<C:
	print("increasing")
elif A>B>C:
	print("decreasing")
else:
	print("NA")