s=" Lwelcome123 #"
alp,dg,sp,sy,up,lw,vw,co=0,0,0,0,0,0,0,0

for i in s:
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up=up+1
		else:
			lw=lw+1
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			co=co+1
	elif i.isdigit():
		dg=dg+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
print("no of alphabets=",alp)
print("no of digits=",dg)
print("no of space=",sp)
print("no of symbol=",sy)		
print("no of vowels=",vw)
print("no of consonants=",co)
print("no of uppercase=",up)
print("no of lowercase=",lw)