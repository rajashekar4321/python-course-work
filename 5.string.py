 #5.string
str1='hello'
str2="world"
str3='''i am rajashekar'''
print(str1)
print(str2)
print(str3)

                    #Operations on Strings

#Concatenation
str1="raja"
str2="shekar"
result=(str1+" "+str2)
print(result)             #raja shekar



# Repetition
print("darling " *4) #darling darling darling darling 
print("123"  * 5)  #123123123123123
print("999" *10)   #999999999999999999999999999999


# Indexing
a="shathakoti"
print(a[2])
print(a[5])
print(a[-1])



# Slicing
print(a[0:6])
print(a[0:10])
print(a[-10:])
print(a[0:])

# Membership
print('sha' in a)
print('shekar' not in a)

              #  Built-in String Functions


# 1. len()
a="love"
print(len(a))


#2. max() and min()
print(min(a))
print(max("rajashekar"))
print(min("rajashekar"))

# a="abcdef"
print(max(a))
print(min(a))

# 3. sorted()
a="lion"
print(sorted(a))
print(sorted("bdca"))

# 4. chr() and ord()
print(ord('A')) 
print(chr(97))



              #1. Case Conversion Methods

a="food is good"
print(a.upper())  #FOOD IS GOOD
print(a.lower())   #food is good
print(a.capitalize())   #Food is good
print(a.title())     #Food Is Good
print(a.swapcase())  #FOOD IS GOOD
print("ß".casefold())  #ss

          #2. Alignment & Formatting Methods


 #center(width,fillchar)         
s="python materal"
print(s.center(10,'*'))
print(a.center(5,"#"))

#ljust(width,fillchar)
print("s".ljust(19,"-"))

#rjust(width,fillchar)
print("s".rjust(9,"*"))

#zfill(width)
print("42".zfill(5))


#format()
print("name:{},age:{}".format("tom",25))


#format_map(mapping)
print("{name} is {age}".format_map({'name':'Tom', 'age': 25}))