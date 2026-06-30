loop:
_______
some statement repeated continously then choose loop
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")
print("A")
print("B")
print("C")


for i in range(3):
	print("A")
	print("B")
	print("C")

function
_____________
some statement repated after some time then choose  function

print("A")
print("B")
print("C")
print("D")
print("A")
print("B")
print("C")
print("E")
print("A")
print("B")
print("C")
print("F")

solve these program using function
_______________________________

def  show():
	print("A")
	print("B")
	print("C")
	return
show()
print("D")
show()
print("E")
show()
print("F")

How to define function
________________

syntax or rule
________________

def  functionname(formal parameter or argument):
	local variable
	logic
	return 

How to call function
____________________

functionname(actual parameter /argument)


we can write function program 4 way
________________________________

(1)no return value no argument
(2)no return value with argument
(3)return value with no argument
(4)return value with argument


# add of two no from keyboard
print("enter a number")
no1=int(input())
print("enter another number")
no2=int(input())
s=no1+no2
print("sum=",s)

(1)no return value no argumnet
def add():
	print("enter a number")
	no1=int(input())
	print("enter another number")
	no2=int(input())
	s=no1+no2
	print("sum=",s)
	return
add()

(2)even or odd using function no return value no argument
def check():
	print("enter a number ")
	no=int(input())
	if no%2==0:
		print("even number ")
	else:
		print("odd number")
check()

(3)find simple interset using function no return value no argument
sical()


def  sical():
	print("enter priniple")
	p=float(input())
	print("enter rate of interset")
	r=float(input())
	print("enter time")
	t=float(input())
	si=p*r*t/100
	print("simple interset=",si)
sical()


(2)no return value with argument

def add(no1,no2):
	s=no1+no2
	print("sum=",s)
add(10,20)





def add(no1,no2):
	s=no1+no2
	print("sum=",s)
print("enter a nnumber")
no1=int(input())
print("enter another number")
no2=int(input())
add(no1,no2)


def check(no):
	if no%2==0:
		print(no,"is even number ")
	else:
		print(no,"is odd number ")
print("enter a nnumber")
no=int(input())
check(no)

def sical(p,r,t):
	si=p*r*t/100
	print("simple interset=",si)
	return 
print("enter priniple")
p=float(input())
print("enter rate of interset")
r=float(input())
print("enter time")
t=float(input())
sical(p,r,t)



return value with no argument
______________________________
def add():
	print("enter a number ")
	no1=int(input(())
	print("enter another number ")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("sum of two no=",res)

evenodd
sical

return value with argument
______________________________
def add(no1,no2):
	s=no1+no2
	return s
print("enter a number ")
no1=int(input(())
print("enter another number ")
no2=int(input())
res=add(no1,no2)
print("sum of two no=",res)


evenodd
sical

why function final 
____________________


1!+2!+3!+4!+5!=155


3!  3*2*1
5!  5 *4*3*2*1

1! 1
0!  1

no=5
f=1
while no>0:
	f=f*no
	no=no-1
print("factorial=",f)






no=5
f=1
s=0
while no>0:
	f=f*no
	no=no-1
s=s+f
no=4
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=3
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=2
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
no=1
f=1
while no>0:
	f=f*no
	no=no-1
s=s+f
print("first 5 factorial sum=",s)


slove using function
__________________

def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=facttest(5)+facttest(4)+facttest(3)+facttest(2)+facttest(1)
print("first 5 factorial sum=",s)



factorila number no return value no argumnet
factorila number no return value with argumnet
factorila number return value with no argumnet

factorila number return value with  argumnet
def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number ")
res=fcattest(int(input()))
print("factorial=",res)
Types of parameter
            _______

(1)requried parameter
(2)default parameter
(3)keyword parameter
(4)variable length parameter


requried parameter
______
def show(a,b,c,d):
	print(a,b,c,d)

show(10,12.34,"hi",5)
#show(1,5,7) error

o/p:
10 12.34 hi 5



default parameter
______

def  show(a=0,b=0,c=10,d=0):
	print(a,b,c,d)
show(5,"hi")
show(1,5,7,12.34)
show()

o/p:
5 hi 10 0
1 5 7 12.34
0 0 0 0



keyword parameter
______

def  show(a=0,b=3,c=10,d=0):
	print(a,b,c,d)
show(1,5,7,12.34)
show(d=25,c=12,a=5,b=1)
show(c=30)
o/p:
1 5  7  12.34
5 1  12  25
0 3 30 0



variable length parameter
_________
1. *args (Variable-Length Positional Arguments)
The *args syntax allows a function to accept any number of positional arguments. Inside the function, args is treated as a tuple.

def show(*a):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
(10, 12.34)
('hi', 1, 5.3)


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Calling with a varying number of arguments
print(multiply(2, 3))          # Output: 6
print(multiply(2, 3, 4))       # Output: 24
print(multiply(1, 2, 3, 4, 5)) # Output: 120







def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with varying keyword arguments
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
print_info(brand="Toyota", model="Corolla", year=2020)
# Output:
# brand: Toyota
# model: Corolla
# year: 2020



def show(*a,b):
	print(a)
show(10,12.34)
show("hi",1,5.3)

o/p:
Traceback (most recent call last):
  File "C:\Users\HP\Desktop\demo.py", line 3, in <module>
    show(10,12.34)
TypeError: show() missing 1 required keyword-only argument: 'b'



def show(b,*a):
	print(a)
show(10,12.34,"hi")
show("bye",1,5.3)
o/p:
(12.34, 'hi')
(1, 5.3)



Combining *args and **kwargs
You can use both *args and **kwargs in the same function. However, *args must come before **kwargs in the function definition.

Example:
def display(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Calling with both positional and keyword arguments
display(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}






______________________________________________
✅ (1) Required Parameter (Positional Parameter)
📘 Theory:
These are mandatory parameters in a function. You must pass values in the correct order. If any required parameter is missing, Python will raise an error.

def add(a, b):
    print("Sum =", a + b)

add(10, 20)     # Correct
# add(10)       # ❌ Error: Missing required argument 'b'
✅ Key Point:
Order matters.

Cannot be skipped.

✅ (2) Default Parameter
📘 Theory:
You can assign a default value to a parameter. If no value is passed, the default is used. If you pass a value, it overrides the default.

def greet(name, msg="Good Morning"):
    print("Hello", name, "-", msg)

greet("Alice")                  # Uses default message
greet("Bob", "Good Evening")   # Overrides default
✅ Key Point:
Must be at the end of the parameter list.

Used to make parameters optional.

✅ (3) Keyword Parameter
📘 Theory:
You pass the argument by name, not by position. This makes your code more readable and the order of arguments doesn't matter.


def student(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student(age=18, grade="A", name="Rita")  # Order doesn't matter
✅ Key Point:
Improves code clarity.

Useful when there are many parameters.

✅ (4) Variable Length Parameter
Python supports two types of variable-length parameters:

🔹 (a) *args → for variable positional arguments
📘 Theory:
Allows passing any number of positional arguments. It stores them as a tuple.


def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(85, 90)
total_marks(70, 80, 90, 95)
🔹 (b) **kwargs → for variable keyword arguments
📘 Theory:
Allows passing any number of keyword arguments. It stores them as a dictionary.


def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="John", age=22, city="Delhi")
🎯 Summary Table:
Type                 Syntax  Use Case                               Stored As
Required Parameter  a, b        Must be passed in order                 Direct values
Default Parameter   a=10       Optional; use default if not passed       Direct values
Keyword Parameter   name="John" Pass by name for readability          Direct values
Variable-length (*args) *args   Pass many positional values            Tuple
Variable-length (**kwargs)  **kwargs    Pass many keyword values    Dictionary