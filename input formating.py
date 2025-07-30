#1 string input
name=input("Enter yoy full name:")
print(name)

#2 integer input
n=(int(input("Enter the number:")))
print(n)

#3 float input
price=float(input("Enter the product price:"))
print(price)

#4 input as list (space-separted)
name=input("Enter the names (space-separted):").split()
print(name)

#5 input as list (comma_separated)
tags=input("Enter tags(comma_separated):").split(',')
print(tags)


#6  List of Integers 
marks=list(map(int,input("Enter marks:").split()))
print(marks)

#8. Tuple Input 
dimensions = tuple(map(int, input("Enter length, width, height: ").split())) 
print(dimensions) 

#9. Set Input 
selected_ids = set(map(int, input("Enter selected image IDs: ").split())) 
print(selected_ids) 


#10. Dictionary Input using eval() 
profile = eval(input("Enter user profile as a dictionary: ")) 
print(profile)



