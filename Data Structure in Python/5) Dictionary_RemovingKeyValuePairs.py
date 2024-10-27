# Example 5: Removing Key-Value Pairs from a Dictionary
# You can remove key-value pairs using the pop() method, which removes the specified key and returns its value.
# The del keyword can also be used to remove a specific key or clear() to remove all items.

# Example dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Removing a key-value pair
age = my_dict.pop('age')

# Printing the dictionary after removal
print('Dictionary after Removal:', my_dict)
print('Removed age:', age)