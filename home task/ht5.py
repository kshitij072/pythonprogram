print("enter side A")
A=int(input())
print("enter side B")
B=int(input())
print("enter side C")
C=int(input())
if A+B>C and B+C>A and C+A>B:
	if A==B and B==C:
		print("equilateral triangle")
	elif A==B or B==C or C==A:
		print("isoceles triangle")
	else:
		print("scalene triangle")





else:
	print("triangle cant be formed")		