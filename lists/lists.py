# Sample lists
fruits = ['apple', 'oranges', 'grapes']
marks = [10, 20, 30]
nested_list = [[1,2], [2,3]]
hetero_list = [1, 'Test', 20.00, ['Nested_list', 20], {1: 'this is a dict inside list'}]

# Accesing list elements:
print(fruits[0]) # prints 'apple'
print(nested_list[1]) # prints [2,3]

# Printing a whole list
for fruit in fruits:
    print(fruit) # Prints each item in the list fruits one by one

# List comprehension

a_list = [a for a in range(1, 10)]
print(a_list) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Methods:

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x]
fruits.append('Mango')
print(fruits) # ['apple', 'oranges', 'grapes', 'Mango']

# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.
fruits.extend(['watermleon', 'guava'])
print(fruits) # ['apple', 'oranges', 'grapes', 'Mango', 'watermleon', 'guava']

# list.insert(i, x)
# Insert an item at a given position.
fruits.insert(1, 'banana')
print(fruits) # ['apple', 'banana', 'oranges', 'grapes', 'Mango', 'watermleon', 'guava']

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.
fruits.remove('guava')
print(fruits) # ['apple', 'banana', 'oranges', 'grapes', 'Mango', 'watermleon']

# list.pop([i])
'''
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list
'''
fruits.pop(0) # apple
print(fruits) # ['banana', 'oranges', 'grapes', 'Mango', 'watermleon']
fruits.pop() # watermelon
print(fruits) # ['banana', 'oranges', 'grapes', 'Mango']

# list.clear()
# Remove all items from the list. Equivalent to del a[:].
fruits.clear()
print(fruits) # []

# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x.
marks.index(10) # 0

# list.count(x)
# Return the number of times x appears in the list.
print([1,2,1,1,3].count(1)) # 3

# list.sort(key=None, reverse=False)
# Sort the items of the list in place.
fruits  = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
fruits.sort()
print(fruits)
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

# list.reverse()
# Reverse the elements of the list in place.
fruits.reverse()
print(fruits) # ['pear', 'orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:]. Will work in Python3 only
fruits.copy()
fruits_copy = fruits.copy()
print(fruits_copy) #['pear', 'orange', 'kiwi', 'grape', 'banana', 'banana', 'apple', 'apple']


