#def function_name(parameters):
   #block of code
#function_name()  


'''def display(name,email,pwd):
    print(name,email,pwd)
name,email,pwd='raja','raja.com','raja122'
display(name,email,pwd)'''


'''def great(name):
    return f"hello,{name}!"
print(great("Alice"))'''


'''def add (a,b):
    return a+b
print(add(5,65))'''

#Function Arguments
def greet(name,age):
    print(f"Hello {name},you are {age} year old.")
greet
print("Alice",25)

# Keyword Arguments
greet(age=25, name="ravi") 


# 1: Function with No Parameters
def great():
    print("hello")
great()


# 2: Function with Parameters
def num(a,b):
    print(a+b)
num(3,5)


#3: Function with Default Parameter
def country(country="india"):
    print("my country:",country)
country("usa")



#4 Function Returning Multiple Values
def cal(a,b):
    return a+b , a-b
c1=cal(2,2)
print(c1)


# Length of a String
text="raja"
print(len(text))


def vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for char in text:
        if char in vowels:
            count +=1
            return count
v1=vowels("rajashekar")
print(v1)


#Count How Many Items in a List Are Greater Than 10

def num(data):
    count=0
    for num in data:
        if num>10:
            count+=10
            return count
n1=num([5,34,4,55,3,67,66]  ) 
print(n1)  

# recursion
def fact(n):
    if n==1 or n==1:
        return n
    else:
        return n*fact(n-1)
f1=fact(5)
print(f1)

#Fibonacci Sequence using recursion
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
f2=fib(6)
print(f2)

        








    
















