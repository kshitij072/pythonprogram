

operator
_________

operator is a symbole that operate the operand.
operand may be varibale constant and expression

unary operator :
it operates one operand .
-5

binary operator :
it operates two operand:
a+b
5*6

ternary operator :
it operates three operand.
in python no ternary operator

?   :

precdence:
it is a table.
it decide which operator evaluate first.

associtive:

more than operator same precdence 
same operator more than in expression
it may be evalute 

left to right 
right to left

*  /  %  //  2  L to R
+ -         3

arithmethic operator
_________________

**  power           10**3    1000      precdence  2     right to left
/   exactly division  10/3     3.33333   precedence 3     Left to right
//  floor  division  10//3    3            "                 "
%    module            10%3    1          "                   "
*     mult              10*3   30         "                  "
+     binary plus       10+3   13         precedence 4       "

-     binary  plus      10-3     7           "               "

unary + -    precdence    2      


precdence
_____________
10+3*2**3


10+3*8
10+24
34


Left to right
_________

10//3*5%2
3*5%2
15%2
1


10*3//4*2
30//4*2
7*2
14



right to left
____________

2**3      
8


2*3*2    
2**9
512




10+5//2
12


10+5/2
12.5






display first digit
_____________________

1258//1000      1
476//100        4
34//10            3
56//10              5

display last digit
_____________________

1258%10     8
476%10       6
34%10       4
56%10       6



last digit delete

_____________________
1258//10      125
476//10       47
34//10        3
56//10         5


a=3
b=10
c=2
a=a+4
b=b//c
c=a+b
print(a,b,c)


o/p:

7 5 12


a=3
b=10
c=2
a=a+4
b=b//c
a+b
print(a,b,c)
o/p:
7 5 2


a=3
print(a+2)
print(a)

o/p:
5
3

a=3
a=a+2
print(a)

o/p:
5


a=3
print(a=a+2)
print(a)

o/p:
error

valid in java c,c++
5
5

unary + - operator
________________

a=5
b=-a
print(a,b)
o/p:
5 -5


add two no without using + operator
________________________________
a=5
b=7
c=a- -b
print("sum=",c)


o/p:
12


increment(++) and decrement(--) operator not avaliable in python.


a=5
++a
print(a)

o/p:
5

in java  c, c++
o/p:
6


a=5
a=a+1
print(a)
o/p:
6


a=5
a+=1
print(a)
o/p:
6



relation operator
_____________
<    lessthan
>    greaterthan
<=   lessthanequal
>=
==   is equal
!=

after compare result true or false

3<5    True
3>5     False
3<=3    True
2<=3    True
4<=3     False
3>=3     True
4>=3  True
4>5    False
3==3     True
3==4     False
3!=4       True

10<20<30    True                    in java error

10<50<30    False

2<3==3>2    True   


print(2<3==3>2)
print(2<3==5>2)

True
False


logical or short circut operator
_________________________________
combine two realtion operator
or   
and 
not

    or 
op1     op2      result
True    True      True
True    False     True
False    True     True
False    False     False

print(True or False)  #True

if first operand is true  second operand not checking.
if first operand  is false  second operand must checking
any nonzero value    true 

3 or 5    3  print(3 or 5)
0 or  5   5
3 or 0    3
0 or 0    0

a=3 
b=5
print(a>2 or b>9) 
print(a<2 or b>9) 
print(a>2 or b<9) 
print(a<2 or b<9) 
o/p:
True
False
True
True


and
op1     op2      result
True    True      True
True    False     False
False    True     False
False    False     False

print(True and False)  #False

if first operand is true  second operand must checking.
if first operand  is false  second operand not checking
any nonzero value    True 

3 and 5    5
0 and  5   0
3 and 0    0
0 and 0    0

a=3 
b=5
print(a>2 and b>9) 
print(a<2 and b>9) 
print(a>2 and b<9) 

o/p:
False
False
True





not 
____


operand   resulet

True       False
False       True


not True    False
not False   True

print(not True)
print(not False)
print( not 5)
print(not not 5)

o/p:

False
True
False
True


identity operator
____________________
is      compare reference
is not

==    compare value

a=10
b=10
c=20
print(a is b)
print(a is c)
print(a is not c)
print(a==b)

o/p:
True
False
True
True

a=[10]
b=[10]
c=[20]
print(a is b)
print(a is c)
print(a is not c)
print(a==b)


o/p:
False
False
True
True


membership operator (in ,not in)

print("n" in "india")  #True
print("ndi" in "india")  #True
print("x" in "india")  #False
print("x" not in "india")  #True
print(10  in [5,7,10,12,34])  #True
print(30  in [5,7,10,12,34])  #False
print(30  not in [5,7,10,12,34])  #True








assginment  operator

  vname =vname/constant/expression
  a=10
  b=20
  10=a  invalid
  10=20  invalid
  a+b=30  invalid

swapping two no using 3rd variable

a=10
b=20
temp=b
b=a
a=temp
print(a,b)

o/p:
20 10


swapping two no without using  3rd variable
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)
or
a=10
b=20
a=a*b
b=a//b
a=a//b
print(a,b)
or
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)



a=10
b=20
a,b=b,a   #(only python)
print(a,b)



compund assginment operator
____________________________

+=
-=
*=
/=
%=
//=
**=
&=
|=
^=
<<=
>>=

a+=3    a=a+3
b*=3   b=b*3

10+=2    error   10=10+2

a+=b*=c+=2   error  (in python)     valid c c++ java

#wap take student name rollno and mark display it
print("enter student name rollno and mark ")
nm=input()
r=int(input())
m=float(input())
print("name=",nm)
print("rollno=",r)
print("mark=",m)
o/p:
enter student name rollno and mark
muna das
1
90.50
name=muna das
rollno=1
mark=90.50

#wap take rectangle length and breadth from keyboard displAY LENGTH 
#breadth  area and perimeter.
print("enter rectagle length ")
L=float(input())
print("enter rectagle breadth ")
B=float(input())
ar=L*B
pr=2*(L+B)
print("length=",L)
print("breadth=",B)
print("area=",ar)
print("perimeter=",pr)

o/p:
enter rectangle length
3.5
enter rectangle breadth
4.5
length=3.5
breadth=4.5
area=
perimeetr=


#simple interset
#sal da ta