#Using Indexing (Positive & Negative)

my_list = ["Python", "Java", "C++"]
print(my_list[0]) 
print(my_list[1]) 
print(my_list[-1])

#Using Slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) # [20, 30, 40]
print(numbers[:3]) # [10, 20, 30] (from start)
print(numbers[2:]) # [30, 40, 50] (to end)
print(numbers[-3:-1]) # [30, 40]
print(numbers[::-1]) # [50, 40, 30, 20, 10] (Reverse list)

#Changing Elements
numbers = [10, 20, 30, 40]
numbers[2] = 100
print(numbers) # [10, 20, 100, 40]

#Adding Elements
# Append (adds to the end)
numbers.append(50)
# Insert (adds at a specific position)
numbers.insert(1, 15)
# Extend (adds multiple elements)
numbers.extend([60, 70, 80])
print(numbers) # [10, 15, 20, 100, 40, 50, 60, 70, 80

#Removing Elements
numbers.remove(100) # Removes first occurrence of 100
numbers.pop(2) # Removes element at index 2
numbers.pop() # Removes last element
del numbers[1] # Deletes element at index 1
numbers.clear() # Clears the entire list

#List Methods
numbers = [3, 1, 4, 1, 5, 9]
print(numbers.count(1)) # 2
print(numbers.index(4)) # 2
numbers.sort()
print(numbers) # [1, 1, 3, 4, 5, 9]
numbers.reverse()
print(numbers) # [9, 5, 4, 3, 1, 1]

#Copying a List
# Shallow Copy
list1 = [1, 2, 3]
list2 = list1.copy()

#Sorting and Reversing Lists

numbers = [5, 3, 8, 2]
numbers.sort() # [2, 3, 5, 8]
numbers.sort(reverse=True) # [8, 5, 3, 2]
numbers.reverse() # [2, 3, 5, 8]