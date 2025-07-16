empty_tuple = ()
my_tuple = (10, 20, 30, 40)
print(my_tuple[2]) # Output: 30

#Accessing Tuple Elements
#a. Indexing
r=(1,2,3,4,5)
print(r[3])

#b. Negative Indexing
a=(1,2,3,4,5)
print(a[-3])

#c. Slicing
r=(1,2,3,4,5)
print(r[1:4])

#3. Operations on Tuples
#a. Concatenation
a=(9,8)
b=(5,4)
print(a+b)

#b. Repetition
a=(1,2)
print(a*4)

#c. Membership Testing
s= (1, 2, 3)
print(2 in s) # Output: True
print(5 not in s) # Output: True

#d. Tuple Unpacking
a=(1,5,8)
a,b,c=a
print(a,b,c)

