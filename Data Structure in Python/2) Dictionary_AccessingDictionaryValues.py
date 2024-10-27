# Example 2 : Accessing Dictionaries Values
# Values in a Dictionary are accessed using their keys
# if a key is not found, a key error will be raised unless you use the get() method, which returns None.

# Example Dictionary
my_dict = { 'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing values using keys
name = my_dict['name']
age = my_dict.get('age')

# Printing accessed values
print('Name:', name)
print('Age:', age)