# Creating a set with unique elements
my_set = {1, 2, 3, 4}
# Creating an empty set (use set() function, not {})
empty_set = set()

set_with_duplicates = {1, 2, 2, 3, 4}
print(set_with_duplicates) # Output: {1, 2, 3, 4}

#2. Set Properties

invalid_set = {[1, 2], 3} # Lists are mutable and cannot be added to a set