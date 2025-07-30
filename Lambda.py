#syntax
#lambda arguments: expression 
greet=lambda:print("hello")
greet()

#with arguments
greet=lambda name:print("my name:",name)
greet("raja")

square=lambda a:a*a
s1=square(3)
print(s1)


sum=lambda a,b:a+b
s2=sum(2,7)
print(s2)


even_or_odd=lambda x:"even"if x%2==0 else "odd"
e1=even_or_odd(6)
print(e1)